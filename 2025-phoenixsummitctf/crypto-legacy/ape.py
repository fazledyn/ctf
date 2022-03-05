from sympy.ntheory.residue_ntheory import discrete_log
from hashlib import sha1, sha256, md5
from Crypto.Cipher import AES
import binascii
import string

# Parameters
# p = 14060974547413669781
# g = 5
# A = 6793340055737354429
# B = 4967934839438925548
# cipher_hex = '5154525043535152576e505a595e4539'

p = 14060974547413669781
g = 5
A = 13498104295969395658
B = 7019788272572177613
cipher_hex = '515f505242555c06550f540a071c000d07021d03020754140f5c570115510a540803070f57520007504833'

# Step 1: Solve Alice's private key
print("[*] Solving discrete log...")
a = discrete_log(p, A, g)
print(f"[+] Found Alice's private key: {a}")

# Step 2: Compute shared secret
s = pow(B, a, p)
print(f"[+] Shared secret: {s}")

# Key derivation candidates
key_candidates = [
    str(s).encode(),                         # raw number bytes
    s.to_bytes((s.bit_length() + 7) // 8, 'big'),  # integer as bytes
    sha1(str(s).encode()).digest(),
    sha256(str(s).encode()).digest(),
    md5(str(s).encode()).digest()
]

cipher_bytes = bytes.fromhex(cipher_hex)

def is_mostly_printable(data):
    return sum(c in string.printable.encode() for c in data) / len(data) > 0.9

# XOR decryption
print("\n[*] Trying XOR decryption with candidate keys...")
for key in key_candidates:
    key_stream = key * (len(cipher_bytes) // len(key) + 1)
    decrypted = bytes(c ^ k for c, k in zip(cipher_bytes, key_stream))
    if is_mostly_printable(decrypted):
        print(f"[+] XOR key {key.hex()}: {decrypted.decode(errors='replace')}")
    else:
        print(f"[-] XOR key {key.hex()} gave non-printable output")

# AES decryption
print("\n[*] Trying AES decryption (ECB)...")
for key in key_candidates:
    if len(key) >= 16:
        aes_key = key[:16]
        cipher = AES.new(aes_key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(cipher_bytes)
            if is_mostly_printable(decrypted):
                print(f"[+] AES key {aes_key.hex()}: {decrypted.decode(errors='replace')}")
            else:
                print(f"[-] AES key {aes_key.hex()} gave non-printable output")
        except Exception as e:
            print(f"[!] AES key {aes_key.hex()} error: {e}")
