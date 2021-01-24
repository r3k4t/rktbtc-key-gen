from bitcoin import *

os.system("clear")

print ("            =============================================")
print ("                          RktBtc-Key-Gen                 ")
print ("            =============================================")
print ("                   Author : Rahat Khan Tusar(rkt)        ")
print ("                   Github : https://github.com/r3k4t     ")
print ("            =============================================")

print 

# Generate private key

rkt_private_key = random_key()
print ("Private key : %s\n"% rkt_private_key)

# Generate public key

rkt_public_key = privtopub(rkt_private_key)
print ("Public Key : %s\n"%rkt_public_key)
