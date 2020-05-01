import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (socket.gethostname(), 9999)

s.sendto('\nHello, from client...!'.encode(), address)
print('\n')

while True:		# continuous stream of bytes

	message = raw_input('root~#: ')
	s.sendto(message.encode(), address)

	if message == 'exit':
		s.close()
		break

	# data, addr = s.recvfrom(1024)
	# print(data.decode())