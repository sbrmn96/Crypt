# SHA 256 Performance evaluation

import timeit
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

start = '''
import timeit
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
'''

stop = '''
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(bytes(256*1000*1000))
digest.finalize()
'''


def SHA_256(message):              
    hash_object = hashlib.sha256(message)
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend()) 
    digest.update(message) 
    msg_digest = digest.finalize() 
    return msg_digest

if __name__ == "__main__":
    byte_plaintext = bytes(1000*1000*256 - 33) #33 bytes are subtracted because of the extra byte header
    digest = SHA_256(byte_plaintext) 
    digest_hex = digest.hex() 
    print("Representation of SHA256 of 256MB zeros")
    print("The Message digest after SHA256 hashing is: \n{} ".format(digest_hex))
    total_time = timeit.timeit(setup=start, stmt=stop, number=10)  
    exec_time = total_time/10
    print("The Average Time taken for Hashing the plaintext: {} seconds".format(exec_time))
    perf = 256/exec_time
    print("The performance of the hashing function is {} MB/s".format(perf))