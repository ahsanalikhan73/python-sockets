import socket
import sys

# python filename.py target-IP
target = sys.argv[1]  # target-IP

for x in range(1, 1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        try:
            s.connect((target, x))
            print('Port {} is Open...!'.format(x))
            s.close()
        except:
            print('Port {} is Closed...!'.format(x))
            s.close()

    except KeyboardInterrupt:
        print('\n[-] Exitting ...!')
        sys.exit()