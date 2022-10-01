#Cherukuri Chandan
#Server With RSA
import socket
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
#from Crypto.Cipher import AES, PKCS1_OAEP
import binascii

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creating a new socket SOCK_STREAM for TCP protocol
socket_obj.bind((socket.gethostname(), 1024))#finds the hostname
socket_obj.listen(5)#listens for 5 secs for packets
#**************** Message Prep Part******************************
message="hello"
hasher=hashlib.sha256()
sendermessage=(message).encode()
hasher.update(sendermessage)
finalmessage=message+"$$$$$"+hasher.hexdigest()

#******************Encryption Part ******************************
print ("Server is ready")

data = finalmessage.encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)

ciphertext=cipher_rsa.encrypt(data)
file_out.write(ciphertext) 
file_out.close()
#*******************Sending Encrypted message Part***************
messagefile = open("encrypted_data.bin","rb")
encryptedmessage=messagefile.read()

clientsocket, address = socket_obj.accept()
print ("Got connection from", address )
print("message:-Hello client this is server")

clientsocket.send(encryptedmessage)
message = clientsocket.recv(10).decode("utf-8")
print("Received: ",message) 

socket_obj.close()