# client.py
# 	thornlea-coin client

import socket

server_address = ('192.168.0.197', 10000)

# Utility functions
def recv_msg(conn, bytes, encoding = 'ascii'):
    return conn.recvmsg(bytes)[0].decode(encoding)

def send_msg(conn, msg):
	conn.sendmsg([msg.encode()])

# Initialize connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
send_msg(sock, "node_new")

seed_ip = recv_msg(sock, 100)
seed_uid = recv_msg(sock, 100)
print(seed_ip)
print(seed_uid)


sock.close()
