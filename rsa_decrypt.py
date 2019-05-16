public_key = (5, 321765937)
private_key = (257379725, 321765937)

#Encryption
message = [ord(c) for c in input()]
encrypted_message = []
for i in message:
    encrypted_message.append(i**public_key[0]%public_key[1])

#Decryption
for i in encrypted_message:
    print(chr(i**private_key[0]%private_key[1]),end='')
print()