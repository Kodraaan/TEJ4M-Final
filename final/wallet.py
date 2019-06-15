# wallet.py
# created june 10, 2019

# acts as a user interface to check balance and make transactions
# enters the network to grab blockchain, check balance by parsing the current block
# sends transactions to network neighbours, when a miner receives it they will verify


import os.path
from pathlib import Path
from uuid import getnode as get_mac
from utils import *

# Check a users balance
def get_balance(wallet_id):
    seed_ip = find_seed(protocols['seed_server']['node_wallet'])
    sock.connect((seed_ip, 8765))

    msg = generate_msg([protocols['all']['no_broadcast'], protocols['wallet']['get_block']])
    send_msg(sock, msg) # protocols.get_block

    block_data = decode_msg(recv_msg(sock, 1000))

    balance = 0
    # we must go through each event in the block and trace the relevant ones to get our balance
    
    return balance

# Send coins to a wallet id
def send_coins(recipient, amount):
    seed_ip = find_seed(protocols['seed_server']['node_wallet'])
    sock.connect((seed_ip, 8765))

    transaction_msg = generate_msg([protocols['all']['broadcast'], protocols['all']['make_transaction'], ])
    transaction_msg = str(protocols.all.make_transaction) + "recipient=" + str(recipient) + ",amount=" + str(amount)
    send_msg(sock, transaction_msg)
    transaction_success = recv_msg(sock, 100)

    return transaction_success




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





# the main loop, from here the user can interact with the program
while True:
    print("Select operation:\n[1] Check balance\n[2] Make transaction")
    command = input()
    if command == "1":
        balance = get_balance(wallet_id)
        print("The balance is " + balance)

    elif command == "2":
        print("Enter wallet id of the recipient:")
        recipient = input()
        print("Enter amount of coins to send:")
        amount = input()
        transaction_success, message = send_coins(recipient, amount)
        if transaction_success:
            print("Transaction Success!")
        else:
            print("Transaction Failure: " + message)





sock.close()
