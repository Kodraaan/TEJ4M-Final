# utils.py
# created june 13, 2019

# utility functions used in the miner, wallet, and/or seed server

import socket
import json

seed_server = ('192.168.0.197', 8765) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

    msg = generate_msg([protocols['all']['no_broadcast'], conn_type])
    send_msg(sock, msg)

    seed_ip = recv_msg(sock, 100)
    print("found a node, ip: " + seed_ip)

    return seed_ip

# get type of a variable, as a string
def get_type(i):
    return type(i).__name__

# Convert data to message to send over TCP
def generate_msg(data):
    msg = b''

    for i in data:
        var_type = get_type(i)
        if var_type == "bool":
            msg += bytes([i])
        elif var_type == "int":
            msg += (i).to_bytes(4, byteorder="big")
        elif var_type == "str":
            msg += i.encode()
        elif var_type == "long":
            msg += (i).to_bytes(8, byteorder="big")

    return msg


def decode_msg(data):
    return tcp_message(data)

class tcp_message:
    def __init__(self, data):
        self.broadcast = data[0]
        self.msg_type = int.from_bytes( data[1:5], "big")
        self.data = data[5:]