# Comp Eng project log

## May 1:
Pi was set up. Packages were updated and ssh was set up for remote connections so that both of us can work on it at the same time. Key pairs were generated so that future connections remain secure but passphrase is not neseccary so time saved. Initial python testing code was run via the socket library for TCP and was successful.

## May 2:
Looks like the parameter for connection.recv() describes how many characters received at once instead of bits/bytes received. Investigation: why does the code send a small message for every chunck? 

## May 6:
Used ssh-keygen to allow us ssh access to the pi without using the password. This will only work for our machines. Experimented with sending messages via TCP to and from the pi.

## May 7:
Started work on a primitive blackjack game in python using the client-server model. The pi runs a TCP server and acts as the dealer, any client can connect and play a game of blackjack. 

## May 8:
Completed minimum viable product of the blackjack game including most game rules. This served as a valuable learning experience for TCP communication, python3 syntax, and the python socket library.

## May 9:
Started cryptocurrency peer-to-peer client code. Resolved the issue of not being able to find the client's own IP address. More blackjack game code debugging.

## May 13:
More research and successful implementation of RSA Encryption.

## May 16:
Cryptocurrency networking solution: whenever a new node wants to join the network, it is first directed to a seed server, in our case the pi, where it obtains an address of a member of the network (first one in its queue of member nodes) and asks to be connected with that member. After each request handled by the seed server, it adjusts its queue so that the newcomer joins the end of the queue, then the first in queue is removed and rejoins at the end. Each node that joins the network also keeps track of its neighbours. Specifically, it adds one to the neighbour list when it first joins a node in the network and when another newcomer asks to join. However, if a newcomer queries for a member that is offline, that newcomer will report that the member is missing to the seed server where the server deletes that member from the queue and assign the newcomer another member. This process repeats as many times as necessary. Also, every member on the network is regularly checking for if all of its neighbours are online. If not, it will ask the seed server for a connection, like a newcomer, and be connected with another member. The seed server would delete the existing node from its queue before adding it to the back and perform the aforementioned procedure. This way, whenever a member wants to broadcast a message, ie a transaction, it will pass the message on to all of its neighbours, which passes on to all of their neighbours (minus the neighbour where it heard the message from), until the message is propagated in the network.