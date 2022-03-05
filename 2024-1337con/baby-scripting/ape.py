from pwn import *


conn = remote('103.191.240.170', 9999)
conn.recvline()

while True:
	intext = conn.recvline()

	try:
		intext = intext.decode("utf-8").strip()
		print(str.encode(intext))
		intext = intext[::-1] + "\r\n"

		print("Sending -- ", intext)
		conn.send(str.encode(intext))
	except:
		print("except")
		break

