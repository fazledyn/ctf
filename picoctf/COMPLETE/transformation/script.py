# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

def decrypt():
    ct = open("enc", "r").read()
    pt = ""
    for i in range(0, len(ct)):

        pt += chr(ord(ct[i]) >> 8)
        pt += chr(0b0000000011111111 & ord(ct[i]))

    print(pt)

if __name__ == "__main__":
    decrypt()

## flag: picoCTF{16_bits_inst34d_of_8_04c0760d}