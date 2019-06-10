# wallet.py
# created june 10, 2019

# acts as a user interface to check balance and make transactions
# enters the network to grab blockchain, check balance by parsing the current block
# sends transactions to network neighbours, when a miner receives it they will verify

import socket
import os.path
from pathlib import Path
from uuid import getnode as get_mac

offline_debug_mode = True
seed_server = ('192.168.0.197', 8765) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

# Find a new seed node
def find_seed():
    if not offline_debug_mode:
        print('connecting to seed server {} port {}'.format(*seed_server))
        sock.connect(seed_server)
        send_msg(sock, "node_wallet")

        seed_ip = recv_msg(sock, 100)
        print("found a node, ip: " + seed_ip)
    else:
        seed_ip = "0.0.0.0"

    return seed_ip

# Check a users balance
def get_balance(wallet_id):
    seed_ip = find_seed()
    sock.connect((seed_ip, 8765))
    send_msg(sock, "get_block")
    block_data = recv_msg(sock, 1000)
    # we must go through each event in the block and trace the relevant ones to get our balance
    
    return 0





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



# the main loop, from here the user can interact with the program
while True:
    print("Select operation:\n[1] Check balance\n[2] Make transaction")
    command = input()
    if command == "1":
        balance = get_balance(wallet_id)
        print("The balance is " + balance)
    elif command == "2":
        print("Make transaction...")






sock.close()
