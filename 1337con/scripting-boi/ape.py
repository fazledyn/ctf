from pwn import *

conn = remote('103.191.240.170', 9998)
conn.recvline()

while True:
	intext = conn.recvline()
	print("intext = ", intext)

	try:
		intext = intext.decode("utf-8").strip()
		intext_list = intext.split(" ")

		numtext = intext_list[-1]
		l = len(numtext)
		print(numtext, l)

		total = 0
		for each in numtext:
			total += int(each)

		a, b = numtext[:l//2], numtext[l//2:]
		a, b = int(a), int(b)
		c = a ^ b
		c = oct(c)[2:]

		print("Sending -- ", str.encode(c))
		conn.send(str.encode(c + "\n"))
	except:
		print("except")
		break
