import socket
import sys
from random import randint

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)  # not sure what this is, it fixed a weird bug

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('192.168.0.197', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

def newcard():
    return randint(1, 10)

def startgame():
    dealer = [newcard(), newcard()]
    player = [newcard(), newcard()]
    return dealer, player, 1

def maketurn(player, dealer, move):
    player_score = sum(player)
    dealer_score = sum(dealer)
    if move == 1 and player_score == 21:
        return 0, ''
    elif move == 1 and dealer_score == 21:
        return 1, ''
    elif player_score > 21:
        return 2, ''
    elif dealer_score > 21:
        return 3, ''
    else:
        return 4, 'Make a turn!'

def dealerturn(dealer):
    if sum(dealer) < 17:
        dealer.append(newcard())
        print('dealer sum is ' + str(sum(dealer)))

while True:
    print('Waiting for a connection...')
    connection, client_address = sock.accept()
    print('Starting blackjack game with', client_address)
    standing = False

    dealer, player, move_num = startgame()
    while True:
        code, msg = maketurn(player, dealer, move_num)
        move_num += 1

        if standing:
            msg = ''
        client_message = 'you have ' + str(sum(player)) + ', dealer shows ' + str(dealer[1]) + '\n' + msg
        connection.sendmsg([str.encode(client_message)])

        print('code is ' + str(code))
        if code == 4: # Player must make a move
            if standing == False:
                print('get player move')
                move, anc, flags, addr = connection.recvmsg(5)
                move = move.decode('ascii').lower()
                while not move:
                    move, anc, flags, addr = connection.recvmsg(5)
                    move = move.decode('ascii').lower()
                # this issue right now is if the game doesn't end after the player hits
                
                print('player move is ' + move)
                if move == 'hit':
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
    


    messages = [
        'Player blackjack! Player wins!',
        'Dealer blackjack! Dealer wins!',
        'Player bust! Dealer wins!',
        'Dealer bust! Player wins!',
        '',
        'Dealer wins!',
        'Player wins!'
    ]

    print(code)
    print(messages[code])
    client_message = 'Player had ' + str(player) + ' = ' + str(sum(player)) + ', Dealer had ' + str(dealer) + ' = ' + str(sum(dealer)) + '\n' + messages[code]
    connection.sendmsg([str.encode(client_message)])

    # Clean up the connection
    connection.close()