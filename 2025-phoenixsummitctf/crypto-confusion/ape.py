from Crypto.Util.Padding import unpad
from binascii import unhexlify, hexlify

# === INPUTS YOU NEED ===

# Replace this with the actual hex string printed in:
# print("The secret", encrypt(FLAG))
flag_ciphertext = input("Enter the secret ciphertext (hex): ").strip()

# Simulate the decrypt function (using ECB decryption oracle)
# You need to connect this to the original decrypt() function
def oracle_decrypt_block(ciphertext_hex_block):
    # Simulate user input to the original program
    print(f"Sending ciphertext block to decrypt(): {ciphertext_hex_block}")
    decrypted_hex = input(f"Enter plaintext = (output from decrypt({ciphertext_hex_block})): ").strip()
    return bytes.fromhex(decrypted_hex)

# === PROCESS THE CIPHERTEXT ===

# Extract IV (first 16 bytes → 32 hex chars)
iv = bytes.fromhex(flag_ciphertext[:32])
cipher_blocks_hex = [flag_ciphertext[i:i+32] for i in range(32, len(flag_ciphertext), 32)]

plaintext_blocks = []
prev = iv

for i, block_hex in enumerate(cipher_blocks_hex):
    # Use oracle to decrypt ciphertext block under ECB
    decrypted_block = oracle_decrypt_block(block_hex)

    # XOR with previous cipher block (or IV for first block)
    plaintext_block = bytes(a ^ b for a, b in zip(decrypted_block, prev))
    plaintext_blocks.append(plaintext_block)

    # Update prev
    prev = bytes.fromhex(block_hex)

# Concatenate plaintext blocks
padded_plaintext = b''.join(plaintext_blocks)

# Remove padding
try:
    plaintext = unpad(padded_plaintext, 16)
except ValueError:
    plaintext = padded_plaintext  # if no padding

print("\nRecovered plaintext:")
print(plaintext.decode(errors="replace"))

