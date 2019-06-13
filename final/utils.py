# utils.py
# created june 13, 2019

# utility functions used in the miner, wallet, and/or seed server

import socket
import json

with open("protocols.json", "r") as f:
    protocols = json.load(f)

# Receive a messages length bytes over conn
def recv_msg(conn, bytes, encoding = 'ascii'):
    return conn.recvmsg(bytes)[0].decode(encoding)

# Send message msg over conn
def send_msg(conn, msg): 
    conn.sendmsg([msg.encode()])

# Find a new seed node
def find_seed(conn_type):
    print('connecting to seed server {} port {}'.format(*seed_server))
    sock.connect(seed_server)
    send_msg(sock, conn_type)

    seed_ip = recv_msg(sock, 100)
    print("found a node, ip: " + seed_ip)

    return seed_ip

def get_type(i):
    return type(i).__name__


# Convert data to message to send over TCP
def generate_msg(data):
    msg = b''

    for i in data:
        if get_type(i) == "bool":
            print("hello world")

        