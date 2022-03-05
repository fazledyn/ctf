from secret import FLAG, hex_to_bin, oct_to_bin
from Crypto.Util.number import *
import random

def Funny(s):
    s_list = list(s)    
    num_to_replace = len(s_list) // 3
    indices_to_replace = random.sample(range(len(s_list)), num_to_replace)
    for i in indices_to_replace:
        s_list[i] = '?'
    return ''.join(s_list)

def bin_to_oct(num):
     result = ""
     for i in range(0, len(num), 3):
          result += oct(int(num[i : i + 3], 2))[2:]
     return result
          

def bin_to_hex(num):
     result = ""
     for i in range(0, len(num), 4):
          result += hex(int(num[i : i + 4], 2))[2:]
     return result


pt = bytes_to_long(FLAG)
e = 0x10001
p = getPrime(1296)
q = getPrime(1296)
n = p * q
ct = pow(pt, e, n)


p_bin = bin(p)[2:]
q_bin = bin(q)[2:]

k = len(p_bin) // 3

p_parts = [p_bin[:k], p_bin[k:2 * k], p_bin[2 * k:]]
q_parts = [q_bin[:k], q_bin[k:2 * k], q_bin[2 * k:]]

p_hints = [p_parts[0], bin_to_oct(p_parts[1]), bin_to_hex(p_parts[2])]
q_hints = [q_parts[0], bin_to_oct(q_parts[1]), bin_to_hex(q_parts[2])]

assert int(p_bin, 2) == int("".join([p_hints[0], oct_to_bin(p_hints[1]), hex_to_bin(p_hints[2])]), 2)
assert int(q_bin, 2) == int("".join([q_hints[0], oct_to_bin(q_hints[1]), hex_to_bin(q_hints[2])]), 2)

p_hints = [Funny(hint) for hint in p_hints]
q_hints = [Funny(hint) for hint in q_hints]


print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")
print(f"p_hints = {p_hints}")
print(f"q_hints = {q_hints}")
