import Crypto.PublicKey.RSA as RSA
import Crypto.PublicKey.DSA as DSA
import Crypto.PublicKey.ElGamal as ElGamal
import Crypto.Util.number as CUN
import os
import hashlib

plaintext = 'P'
another_text = 'The rain in Spaim falls mdainly on the Plain'


# Here is a hash of the message
# hash = MD5.new(plaintext.encode()).digest()
another_hash = hashlib.sha256(another_text.encode()).digest()
hash = hashlib.sha256(plaintext.encode()).digest()
print(repr(hash))
# '\xb1./J\xa883\x974\xa4\xac\x1e\x1b!\xc8\x11'

# Generates a fresh public/private key pair
key = RSA.generate(1024, os.urandom)

if RSA == DSA:
    K = CUN.getRandomNumber(128, os.urandom)
elif RSA == ElGamal:
    K = CUN.getPrime(128, os.urandom)
    while CUN.GCD(K, key.p - 1) != 1:
        print('K not relatively prime with {n}'.format(n=key.p - 1))
        K = CUN.getPrime(128, os.urandom)
    # print('GCD({K},{n})=1'.format(K=K,n=key.p-1))
else:
    K = ''

# You sign the hash
signature = key.sign(hash, K)
print(len(signature), RSA.__name__)
import sys
print(sys.getsizeof(signature))
# (1, 'Crypto.PublicKey.RSA')
# (2, 'Crypto.PublicKey.DSA')
# (2, 'Crypto.PublicKey.ElGamal')

# You share pubkey with Friend
pubkey = key.publickey()

# You send message (plaintext) and signature to Friend.
# Friend knows how to compute hash.
# Friend verifies the message came from you this way:
print (pubkey.verify(another_hash, signature))

# A different hash should not pass the test.
print (not pubkey.verify(hash[:-1], signature))