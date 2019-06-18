# miner.py
# created june 10, 2019

# acts as a node in the network, will verify any transactions sent through it
# when a miner verifies a transaction they are allowed to include their own wallet address in the message: they will be rewarded

from utils import *
import os
from multiprocessing import Lock, Process, Value, current_process

offline_debug_mode = True

# TODO: listen_for_transaction

# TODO: listen_for_block (wait)

def pack_block(transactions, past_block):
    # transactions is a list of transactions
    # past_block is a byte object
    new_block = b''

# TODO: verify transaction

# TODO: complete_block
def mine(block):
    pass

# Initialization
if not offline_debug_mode:
    sock.connect(seed_server)
    send_msg(sock, protocols['miner']['node_miner'])
    seed_add = recv_msg(sock, 4) # 4 bytes for ipv4 address?
    sock.connect(seed_add)
    # TODO: catch up on recent trasactions