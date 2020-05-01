import socket
import sys

s  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999

s.sendto('Hello from client'.encode(), (host, port))
print('\n')

while True:
	data = raw_input('root~#: ')
	s.sendto(data.encode(), (host, port))

	if data == 'exit':
		print('\n[-] Exiting...')
		s.close()
		sys.exit()


