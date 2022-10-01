#Cherukuri Chandan
#Client With RSA
import socket
import hashlib
from Crypto.PublicKey import RSA
#from Crypto.Cipher import AES, PKCS1_OAEP
import binascii

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect((socket.gethostname(), 1024))
message = socket_obj.recv(1024)
print("Received: ",message)
ciphertext=message
#**********RSA Private Key Decryption**************************
recipient_key = RSA.import_key(open("private.pem").read())

cipher_rsa = PKCS1_OAEP.new(recipient_key)
decryption=cipher_rsa.decrypt(ciphertext)

#**********Checks the integrity of the Hash value*************
def integrity(decryption):   
    prehash=str(decryption).split("$$$$$")
    hashval=prehash[1]
    message=prehash[0]
    hasher=hashlib.sha256()
    message=message.lstrip("b'")
    hashval=hashval.rstrip("'")
    sendermessage=(message).encode()
    print("this is message is ",message)
    hasher.update(sendermessage)
    integrity=str(hasher.hexdigest())
    if(integrity==hashval):
        print("The message is safe")
    else:
        print("We are doomed Do not trust me")
integrity(decryption)
print("Sending:-connection acknowledged")
socket_obj.send("connection acknowledged".encode("utf-8"))

socket_obj.close()