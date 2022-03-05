from secrets import token_bytes
from itertools import cycle, product

flag_enc = bytes.fromhex("a177109a8d0b5abc98536d98bf584f8ad25702dbbf0f57e1847b6c81bf1d53e6bc17338b9d")
print(flag_enc)

not_solved = True

while not_solved:

    wee = token_bytes(8)
    cipher = ''

    dec = bytes([ a ^ b for a, b in zip(flag_enc, cycle(wee))])

    try:
        cipher = dec.decode("utf-8") + "\n"

        if "Bsides" in cipher:
            print(cipher)
            not_solved = False
    
    except:
        pass



# for secret in FLAG:
# 	enc = bytes([ a ^ b for a,b in zip(secret, cycle(wee)) ])
# 	cipher += enc.hex() + '\n'

# open("flag.enc", "w").write(cipher)