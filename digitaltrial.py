import hashlib
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
#************Hashing the plaintext******************
plaintext=input("Enter the plain text : ")
hasher=hashlib.sha256()
hasher.update(plaintext.encode())
data=hasher.hexdigest()

#************Encrypting the hash********************
publickey = RSA.import_key(open("receiver.pem").read())
cipher_rsa = PKCS1_OAEP.new(publickey)
digitalsign=cipher_rsa.encrypt(data.encode())

print("This is the encrypted digital signature ",digitalsign)

print("**********************************************")
#***********Decrypting the digital signature*********
privatekey = RSA.import_key(open("private.pem").read())
decrypt_rsa = PKCS1_OAEP.new(privatekey)
decryption=decrypt_rsa.decrypt(digitalsign)

#**********Verifying the digital signature*********
if(data.encode()==decryption):
    print("The digital signature is verified")
else:
    print("This is a fake signature")
print("This is the decrypted digital signature",decryption)



