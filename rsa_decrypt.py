public_key = (3, 253)
private_key = (147, 253)

#Encryption
message = [ord(c) for c in input()]
encrypted_message = []
for i in message:
    encrypted_message.append(i**public_key[0]%public_key[1])

#The encrypted message (nonsense)
for i in encrypted_message:
    print(chr(i),end='')
print()

#Decryption
for i in encrypted_message:
    print(chr(i**private_key[0]%private_key[1]),end='')
print()

#TODO: remember checking out pow(ord(char),key,n) 