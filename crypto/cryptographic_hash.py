from hashlib import *

hmm = 'a test string ;)'

print(sha256(hmm.encode('ascii')).hexdigest())
print(sha256('aiyayayi'.encode('ascii')).hexdigest())
print(sha256('This is a  rather long string which I hope outputs the same number of output as the other ones'.encode('ascii')).hexdigest())
print(sha256('This is a  rather long string which I hope outputs the same number of output as the other ones'.encode('ascii')).hexdigest())