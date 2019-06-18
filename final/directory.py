# directory.py
# 	Seed node directory server. Allows an entrant to the crypto network find a seed node.

import collections
import socket
from utils import *

server_address = ('192.168.0.197', 8765)    #Using a random port to avoid conflict with anything else
queue = collections.deque()

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('starting directory server on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    conn, client_addr = sock.accept()
    conn_type = recv_msg(conn, 100)
    

    if conn_type == protocols['seed_server']['node_miner'] or conn_type == protocols['seed_server']['node_wallet']:
        # A new node is attempting to connect
        if len(queue) == 0:
            # This is the first node, do nothing
            send_msg(conn, "")
        else:
            # Choose a seed node
            seed_node = queue[0]
            send_msg(conn, seed_node["ip"][0])

        if conn_type == protocols['seed_server']['node_wallet']: # this can be done better, but works for now..
            # Add new node to the queue
            node = {
                "ip": client_addr
            }

            queue.append(node)
            queue.rotate(-1)
    elif conn_type == protocols['seed_server']['node_report']:
        # A network node is making a report
        print("A network node is making a report!")
        

    conn.close()
