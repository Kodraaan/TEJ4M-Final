import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.197', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

def get_msg():
	move = None
	while not move:
		data, ancdata, msg_flags, address = sock.recvmsg(500)
		move = data.decode()
		print('**********' + move + '***********')
	return move


while True:
	print(get_msg())

	move = input().encode()
	if (move == 'quit'):
		sock.close()
		break
	sock.sendmsg([move])

