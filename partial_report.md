# Report - Half way

## Goals
Our goal is to become familiar with creating and managing networks of computers through the use of TCP, as well as a variety of related concepts. We will work on a few projects gradually increasing our knowledge of networking and the workflow for creating client and server applications.

We also intend to explore different options for the development workflow of networking based programs. Some of the tools we will be using are SSH, SFTP, and Git. These tools will allow us to work collaboratively while learning the workflow of real-world development environments.

Our final goal will be to create a simple cryptocurrency using all the knowledge we have acquired. Cryptocurrencies take advantage of dynamic a peer-to-peer network allowing nodes to join and leave at will. The creation of such a network is complicated as, to maintain a functional blockchain, all nodes must remain connected by some path regardless of the changes in which nodes enter or exit the network. Additionally, in order for the currency to be secure and thus viable, we must use elements of cryptography such as digital signatures and RSA encryption, and we must be able to reliably transmit the related data between nodes in the network.

## Our Path So Far



We began by setting up our development environment through the use of Git via Github, SSH for controlling the pi from our laptops, and SFTP for file transfer to the pi.

Our first project was a simple game of blackjack using the client-server model. The pi served as the server, with a client connecting via TCP. The server would generate cards and act as a dealer for the player to play against. This project taught us the necessary information about sockets and TCP, and brought to our attention the power and limitations of the medium as well as the socket library in python.

https://prod.liveshare.vsengsaas.visualstudio.com/join?64C16C842F0743B6875B7299AA4CB1E4FF74