import socket
import sys
from random import randint
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.197', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

def newcard():
    return randint(1, 13)

def startgame():
    dealer = [newcard(), newcard()]
    player = [newcard(), newcard()]
    return dealer, player

def maketurn(player, dealer, move):
    player_score = sum(player)
    dealer_score = sum(dealer)
    if move == 1 and player_score == 21:
        return 0, 'Player Blackjack! Player wins'
    elif move == 1 and dealer_score == 21:
        return 1, 'Dealer Blackjack! Dealer wins'
    elif player_score > 21:
        return 2, 'Player bust! Dealer wins'
    elif dealer_score > 21:
        return 3, 'Dealer bust! Player wins'
    else:
        return 4, 'Make a turn!'

def dealerturn(dealer):
    if sum(dealer) < 17:
        dealer.append(newcard())

while True:
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    print('Starting blackjack game with', client_address)
    move_num = 1
    standing = False

    dealer, player = startgame()
    while True:
        code, msg = maketurn(player, dealer, move_num)
        move_num += 1

        client_message = 'you have ' + str(sum(player)) + ', dealer shows ' + str(dealer[1]) + '\n' + msg
        connection.sendall(str.encode(client_message))

        print('code is ' + str(code))
        if code == 4: # Player must make a move
            if standing == False:
                move, anc, flags, addr = connection.recvmsg(5)
                # this issue right now is if the game doesn't end after the player hits
                move = move.decode('ascii').lower()
                if move == 'hit00':
                    player.append(newcard())
                    dealerturn(dealer)
                elif move == 'stand':
                    standing = True
                    while sum(dealer) < 17:
                        dealerturn(dealer)
            elif standing == True:
                player_score = sum(player)
                dealer_score = sum(dealer)
                code = 5 if dealer_score > player_score else 6
                break
        else:
            break
    
    print('game ended with code ' + str(code))

    # connection.sendall(b'test data')

    # Clean up the connection
    connection.close()