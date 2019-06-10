# wallet.py
# created june 10, 2019

# acts as a user interface to check balance and make transactions
# enters the network to grab blockchain, check balance by parsing the current block
# sends transactions to network neighbours, when a miner receives it they will verify

import socket
import os.path
from pathlib import Path
from uuid import getnode as get_mac

seed_server = ('192.168.0.197', 8765) 

# Utility functions

# Receive a messages length bytes over conn
def recv_msg(conn, bytes, confirm = False, encoding = 'ascii'):
    msg = conn.recvmsg(bytes)[0].decode(encoding)
    if confirm:
        send_msg(conn, "confirm")
    return msg

# Send message msg over conn
def send_msg(conn, msg): 
    conn.sendmsg([msg.encode()])

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

# Grab our wallet id
wallet_id = ""
wallet_file = Path("./wallet_id")
if wallet_file.is_file():
    # read from file
    wallet_id = wallet_file.read_text()
else:
    # generate id (mac address)
    # TODO: hash the mac address so we dont send it to everyone
    wallet_file.touch()
    wallet_id = str(get_mac())
    wallet_file.write_text(wallet_id)

print("Wallet id retreived: " + wallet_id)


# Initialize connection
# TODO: since the server only connects with one node at a time, maybe add collision avoidance or timout/retry code
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting to {} port {}'.format(*seed_server))
sock.connect(seed_server)
send_msg(sock, "node_wallet")

seed_ip = recv_msg(sock, 100)
print("found a node, ip: " + seed_ip)

# Connect to the seed node, and request the block
sock.connect((seed_ip, 8765))
send_msg(sock,"add_neighbour")




sock.close()
