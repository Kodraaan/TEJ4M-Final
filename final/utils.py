# utils.py
# created june 13, 2019

# utility functions used in the miner, wallet, and/or seed server

import socket
import json
import struct

seed_server = ('192.168.0.197', 8765) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with open("protocols.json", "r") as f:
    protocols = json.load(f)

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

# Receive a messages length bytes over conn

def recvall(conn, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def recv_msg(conn):
    # Read message length and unpack it into an integer
    raw_msglen = recvall(conn, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)


# Send message msg over conn
def send_msg(conn, msg):
    msg = struct.pack('>I', len(msg)) + msg
    conn.sendall(msg)

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
            msg += struct.pack('>?', i) #bytes([i])
        elif var_type == "int":
            msg += struct.pack('>I', i) #(i).to_bytes(4, byteorder="big")
        elif var_type == "str":
            msg += i.encode()

    return msg




def encode_transaction(obj):
    pass

class tcp_message:
    def __init__(self, data):
        self.broadcast = data[0]
        self.msg_type = int.from_bytes( data[1:5], "big")
        self.data = data[5:]

class transaction:
    def __init__(self, data):
        self.id = int.from_bytes(data[0:4], 'big')
        self.sender = int.from_bytes(data[4:12], 'big')
        self.recipient = int.from_bytes(data[12, 20], 'big')
        self.sender_ip = int.from_bytes(data[20, 24], 'big')
        self.amount = int.from_bytes(data[24, 28], 'big')
        self.sender_balance = int.from_bytes(data[28, 32], 'big')
        self.sender_public_key = int.from_bytes(data[32, 160], 'big')
        self.signature = int.from_bytes(data[32, 168], 'big')
    # I suggest a function that packs a transaction as well
        
class miner_reward:
    def __init__(self, data):
        self.wallet_add = int.from_bytes(data[:8], 'big')
        self.amount = int.from_bytes(data[8:], 'big')

class balance:
    def __init__(self, data):
        self.wallet_add = int.from_bytes(data[:8], 'big')
        self.balance = int.from_bytes(data[8:], 'big')

def parse_block(block):
    parsed_block = tuple()
    parsed_block += tuple(int.from_bytes(block[:4],'big'))
    parsed_block += tuple(int.from_bytes(block[4:24],'big'))
    transactions = list()
    for i in range(10):
        transactions.append(transaction(block[24+168*i:24+168*(i+1)]))
    parsed_block += tuple(transactions)
    parsed_block += tuple(miner_reward(block[1704:1713]))
    parsed_block += tuple(int.from_bytes(block[1713:1717], 'big'))
    balances = list()
    for i in range(parsed_block[-1]):
        balances.append(balance(block[1717+12*i:1729+12*i], 'big'))
    parsed_block += tuple(balances)
    return parsed_block

def get_current_transactions():
    pass
    # get the current list of transactions


def get_previous_block():  
    pass
    # get previous block