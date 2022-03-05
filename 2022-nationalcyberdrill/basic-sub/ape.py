from pwn import *

p = connect("43.229.15.116", 8101)

payload = asm('sub eax,ebx', arch='x86')

p.send(payload)
p.interactive()