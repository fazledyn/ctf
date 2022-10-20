hexstring = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"

byte_array = bytearray.fromhex(hexstring)
msg = []

for char in byte_array:
    for each_char in range(36, 126):
        if (each_char * 123 + 18) % 256 == char:
            msg.append(chr(each_char))
            break

print("".join(msg))