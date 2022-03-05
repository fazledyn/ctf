#!/usr/bin/python3

# Using this script to get flag

int_list = open("output", "r").read().strip().split("\n")
print("Flag: picoCTF{", end='')

for each in int_list:
	num = int(each, base=10)
	print(chr(num), end='')

print("}")
