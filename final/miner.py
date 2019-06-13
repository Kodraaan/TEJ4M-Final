# miner.py
# created june 10, 2019

# acts as a node in the network, will verify any transactions sent through it
# when a miner verifies a transaction they are allowed to include their own wallet address in the message: they will be rewarded

from utils import *

offline_debug_mode = True
seed_server = ('192.168.0.197', 8765) 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if not offline_debug_mode:
    sock.connect(seed_server)
    