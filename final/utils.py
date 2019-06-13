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



