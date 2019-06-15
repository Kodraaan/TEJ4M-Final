# miner.py
# created june 10, 2019

# acts as a node in the network, will verify any transactions sent through it
# when a miner verifies a transaction they are allowed to include their own wallet address in the message: they will be rewarded

from utils import *

offline_debug_mode = True

if not offline_debug_mode:
    sock.connect(seed_server)
    send_msg(sock, protocols['miner']['node_miner'])
    seed_add = recv_msg(sock, 4) # 4 bytes for ipv4 address?
    sock.connect(seed_add)