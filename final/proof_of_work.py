import random
import hashlib

block = bytes([random.randint(0,255) for i in range(13896)])

while True:
    temp = int(random.random()*1461501637330902918203684832716283019655932542975)
    temp = int.to_bytes(temp, 20,'big')
    hashed = hashlib.sha1(block+temp).hexdigest()
    if hashed[:4] == '0000':
        print('the padding is', temp)
        print('the hash is', hashed)
        break