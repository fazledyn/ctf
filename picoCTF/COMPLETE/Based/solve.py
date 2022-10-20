#!/usr/bin/python3

# Script for converting binary to ASCII

print("Phase 1: Binary")
bin_string = input("Enter bin string: ")
bin_num_list = bin_string.strip().split(" ")

for each in bin_num_list:
	num = int(each, base=2)
	print(chr(num), end='')
print()

print("Phase 2: Octal")
int_string = input("Enter int string: ")
int_num_list = int_string.strip().split(" ")
print(int_num_list)

for each in int_num_list:
	num = int(each, base=8)
	print(chr(num), end='')
print()

print("Phase 3: Hex")
hex_string = input("Enter hex string: ")

bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print(ascii_string)

