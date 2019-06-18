# wallet.py
# created june 10, 2019

# acts as a user interface to check balance and make transactions
# enters the network to grab blockchain, check balance by parsing the current block
# sends transactions to network neighbours, when a miner receives it they will verify


import os.path
from pathlib import Path
from uuid import getnode as get_mac
from utils import *

# Grab our wallet id
wallet_id = ""
wallet_file = Path("./wallet_id")
if wallet_file.is_file():
    # read from file
    wallet_id = wallet_file.read_text()
else:
    # generate id (mac address)
    wallet_file.touch()
    wallet_id = str(get_mac())
    wallet_file.write_text(wallet_id)

print("Wallet id retreived: " + wallet_id)

transaction_list = []

# Connect to a seed node
seed_ip = find_seed(protocols['seed_server']['node_wallet'])
if not seed_ip:
    sock.connect((seed_ip, 8765))
    conn_msg = generate_msg([protocols['all']['no_broadcast'], protocols['wallet']['new_connection']])
    send_msg(sock, conn_msg)

    # get transaction list



# Listen for new connections and transactions
wallet_address = (get_ip(), 8765)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('wallet listening on {} port {}'.format(*wallet_address))
sock.bind(wallet_address)
sock.listen(1)





while True:
    conn, client_addr = sock.accept()
    msg = tcp_message(recv_msg(conn))

    if msg.msg_type == protocols['wallet']['new_connection']:
        pass
        # send the current transaction list

    # broadcast the message
    if msg.broadcast:
        pass
        

    conn.close()




# the main loop, from here the user can interact with the program
# while True:
#     print("Select operation:\n[1] Check balance\n[2] Make transaction")
#     command = input()
#     if command == "1":
#         balance = get_balance(wallet_id)
#         print("The balance is " + balance)

#     elif command == "2":
#         print("Enter wallet id of the recipient:")
#         recipient = input()
#         print("Enter amount of coins to send:")
#         amount = input()
#         transaction_success, message = send_coins(recipient, amount)
#         if transaction_success:
#             print("Transaction Success!")
#         else:
#             print("Transaction Failure: " + message)





sock.close()
