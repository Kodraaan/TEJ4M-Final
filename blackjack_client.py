import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.197', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

data, ancdata, msg_flags, address = sock.recvmsg(500)
print(data.decode())

move = input()
sock.sendall(move.encode())
sock.close()