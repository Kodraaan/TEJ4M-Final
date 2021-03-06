# client.py
# CanadianPesos client

import socket

# Gets its own ip address
def get_ip():
    aiya = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        aiya.connect(('10.255.255.255',1))
        IP = aiya.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        aiya.close()
    return IP

server_address = ('192.168.0.197', 8765)   #Using a random port to avoid conflict with anything else

# Utility functions
def recv_msg(conn, bytes, confirm = False, encoding = 'ascii'):
    msg = conn.recvmsg(bytes)[0].decode(encoding)
    if confirm:
        send_msg(conn, "confirm")
    return msg

def send_msg(conn, msg):
    conn.sendmsg([msg.encode()])

# Initialize connection
# TODO: since the server only connects with one node at a time, maybe add collision avoidance or timout/retry code
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
send_msg(sock, "node_new")

seed_ip = recv_msg(sock, 100, True)
seed_uuid = recv_msg(sock, 100)
print("ip: " + seed_ip)
print("uuid: " + seed_uuid)

# Now connect to that seed node so that they know they have a new neighbour
sock.connect((seed_ip,8765))
send_msg(sock,"add_neighbour")
# Do I need to close the active connection?
sock.bind((get_ip(),8765))
sock.listen(1)
neighbours = []

def broadcast(sock, transaction, source, destination): # passes the socket used, transaction message, where the message was received, and neighbours
    for i in destination:
        if i != source:
            send_msg(sock,transaction)

while True:
    # TODO: listen for connections and broadcast messages
    # Not too sure if broadcasting still requires "solid" connections
    conn, client_addr = sock.accept()
    # TODO: need to add uuid
    neighbours.append(client_addr)

sock.close()
