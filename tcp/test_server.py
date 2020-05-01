import socket

def server():
    s = socket.socket()
    host = socket.gethostname()
    port = 9999

    s.bind((host, port))
    s.listen(5)
    print('\n[+] Waiting for an incomming connection ...!\n')

    conn, addr = s.accept()
    print('[+] Got a connection from ' + str(addr[0]))

    conn.send('\nHello from Server...!'.encode())

    while True:
        message = conn.recv(1024).decode()

        if message.lower().strip() == 'exit':
            conn.close()
            break

        print(message)

        data = raw_input('\nroot~#: > ')
        conn.send(data.encode())
   #s.close()


if __name__ == '__main__':
    server()
