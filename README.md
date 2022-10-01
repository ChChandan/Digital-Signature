# Digital-Signature
A client server model with digital signature authentication

<h1>Steps</h1>
<ol>
<li>Run keygen.py<li>
<li>Run digitaltrial.py<li>
<li>Run server_RSA.py<li>
<li>Run client_RSA.py<li>
</ol>

<h1>Files</h1>
<h4>Keygen.py</h4>
<br/>
This file is used to generate the keys for the encryption and decryption of the data. It creates two files private.pem which hosts the private key used by the server and reciever.pem which hosts the public key of server which is used to encrypt the data.

<h4>Digitaltrial.py</h4>
<br/>
This file is used to encrypt the public key which in turn creates a digital signature


<h4>Server_RSA.py & Client_RSA.py</h4>
<br/>
These are your usual client & server files with RSA encryption which are used to send and recieve the messages


