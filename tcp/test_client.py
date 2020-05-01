import socket
import sys

def client():
	s = socket.socket()
	host = socket.gethostname()
	port = 9999
	s.connect((host, port))

	data = s.recv(1024)
	print(data.decode())

	while True:
            message = raw_input('\nroot~#: > ')
            s.send(message.encode())

            if message == 'exit':
                break        

            data = s.recv(1024)
            print(data.decode())

        s.close()

if __name__ == '__main__':
	client()
