# directory.py
# 	Seed node directory server. Allows an entrant to the crypto network find a seed node.

import collections
import socket
import uuid

server_address = ('192.168.0.197', 8765)    #Using a random port to avoid conflict with anything else
queue = collections.deque()

# Utility functions
def recv_msg(conn, bytes, encoding = 'ascii'):
    return conn.recvmsg(bytes)[0].decode(encoding)

def send_msg(sock, msg, confirm = False):
    sock.sendmsg([msg.encode()])
    if confirm:
        success = recv_msg(sock, 100)
        return success == "confirm" # This can likely be cleaned up

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('starting directory server on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    conn, client_addr = sock.accept()
    conn_type = recv_msg(conn, 20)

    if conn_type == "node_new":
        # A new node is attempting to connect
        if len(queue) == 0:
            # This is the first node, do nothing
            send_msg(conn, "")
        else:
            # Choose a seed node
            seed_node = queue[0]
            send_msg(conn, seed_node["ip"][0], True)
            send_msg(conn, str(seed_node["uuid"]))

        # Add new node to the queue
        node = {
            "uuid": uuid.uuid4(),
            "ip": client_addr
        }

        queue.append(node)
        queue.rotate(-1)
    elif conn_type == "node_wallet":
        print("A wallet is looking for a seed")

    elif conn_type == "node_report":
        # A network node is making a report
        print("A network node is making a report!")
        

    conn.close()
