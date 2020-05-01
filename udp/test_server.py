import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = (socket.gethostname(), 9999)

s.bind(address)

print('\n[+] Waiting for an incomming connection ...!')
data, addr = s.recvfrom(1024)
print('\n[+] Got a connection from ' + str(addr))
print(data.decode())

while True:     # continuous stream of bytes
    data, addr = s.recvfrom(1024)
    print(data.decode())

    if data.decode() == 'exit':
        s.close()
        break

    # message = raw_input('root~#: ')
    # s.sendto(message.encode(), address)