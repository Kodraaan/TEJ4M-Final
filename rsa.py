from hashlib import sha256
p, q = 103, 11
N = p*q
phi_N = (p-1)*(q-1)

def prime_factors(n):   #TODO: may be a lot faster with Euler's GCD
    ans = []
    temp = n
    if n > 0:
        while temp > 1:
            for i in range(2,temp+1):
                if temp%i == 0:
                    ans.append(i)
                    temp = temp//i
                    break
    return ans

def coprime(): #AKA finding e; using instance (global) variables phi_N, N, p and q but N's only prime factors are p and q
    phi_N_factors = prime_factors(phi_N)
    for i in range(2,phi_N):
        found_it = True
        contestant_factors = prime_factors(i)
        for a in contestant_factors:
            if a in phi_N_factors or a in (p,q):
                found_it = False
                break
        if found_it:
            return i
    return None

def find_d(e):
    for i in range(1,phi_N+2):
        if e*i%phi_N == 1:
            return i
    return None

def encrypt(privatek, plaintext):
    #Unpack the key into it's components
    key, n = privatek

    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
            
    numberRepr = [ord(char) for char in plaintext]
    print("Number representation before encryption: ", numberRepr)
    cipher = [pow(ord(char),key,n) for char in plaintext]
    
    #Return the array of bytes
    return cipher


def decrypt(publick, ciphertext):
    #Unpack the key into its components
    key, n = publick
       
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    numberRepr = [pow(char, key, n) for char in ciphertext]
    plain = [chr(pow(char, key, n)) for char in ciphertext]

    print("Decrypted number representation is: ", numberRepr)
    
    #Return the array of bytes as a string
    return ''.join(plain)
    
    
def hashFunction(message):
    return sha256(message.encode("UTF-8")).hexdigest()
    
    
def verify(receivedHashed, message):
    ourHashed = hashFunction(message)
    if receivedHashed == ourHashed:
        print("Verification successful: ", )
        print(receivedHashed, " = ", ourHashed)
    else:
        
        print("Verification failed")
        print(receivedHashed, " != ", ourHashed)

public_key = (coprime(),N)
private_key = (find_d(public_key[0]),N)

print('public:', public_key)
print('private:',private_key)
print('N',N)

# print((2**public_key[0]%public_key[1])**private_key[0]%private_key[1])
