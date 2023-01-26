from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

import math, sys


n = 83232624828177792595616071377000807648193740704003684702730106564705021966450976897666830287374129971840360282835980341277400234100463758607909646621886048089944598200834251938747443355141622459640087876451827639037621380831740452076690631846801487196146179117278789029593215859339250310335337950643729590909

# def keygen(nbit=512):
#     p, q = [ getPrime(nbit) for _ in range(2)]
#     n = p * q
#     phi = (p-1)*(q-1)
#     d = getPrime(1 << 8)
#     e = inverse(d, phi)
#     key = RSA.construct((n,e,d))

#     return key

while True:
    p, q = [ getPrime(512) for _ in range(2) ]

    sys.stdout.write("*")
    sys.stdout.flush()        

    if p * q == n:
        sys.stdout.write("HIT!")
        sys.stdout.write("p:", p)
        sys.stdout.write("q:", q)
        sys.stdout.flush()        
        break


# pubkey = RSA.import_key(open("pubkey.pem", "r").read())

# e = pubkey.e
# n = pubkey.n

# print(f"e: {e}")
# print(f"n: {n}")

# n_bit = int(math.log(e, 2))
# print(f"n_bit (e): {n_bit}")

# n_bit = int(math.log(n, 2))
# print(f"n_bit (n): {n_bit}")


# while True:
#     p = getPrime(n_bit)

#     if n % p == 0:
#         print(p)
#         break

# print(pubkey.d)




# pubkey = open("pubkey.pem", "rb").read()
# ciphertext = open("flag.enc", "rb").read()

# print("Text file read!")

# while True:

#     print("*", end="")

#     nbit = 512
#     key = keygen(nbit)

#     if key.public_key().export_key("PEM") == pubkey:
        
#         print("HIT!!!!!!!")
#         cipher_rsa = PKCS1_v1_5.new(key)
#         dec = cipher_rsa.decrypt(ciphertext)

#         print(str(dec, encoding="utf-8"))
#         break


# FLAG = open('flag.txt', 'rb').read()

# cipher_rsa = PKCS1_v1_5.new(key)
# enc = cipher_rsa.encrypt(FLAG)

# open('flag.enc', 'w').write( enc.hex() )
# open('pubkey.pem', 'wb').write( key.public_key().export_key('PEM') )
