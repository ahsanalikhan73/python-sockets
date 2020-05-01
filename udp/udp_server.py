import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999

s.bind((host, port))

print('\n[+] Waiting for an incomming connection ...!\n')

while True:
    data, addr = s.recvfrom(1024)
    print('[+] Got a connection from ' + str(addr))
    print('\nMessage : ' + data.decode())

    while True:
        data, addr = s.recvfrom(1024)

        if data.decode() == 'exit':
            s.close()
            sys.exit()

        print(data.decode())

