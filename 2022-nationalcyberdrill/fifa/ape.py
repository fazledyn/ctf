import vignere
import string

def main():

	print("-------------------")
	print("| Vigenere Cipher |")
	print("-------------------\n")

	vc = vignere.VigenereCipher()

	charset = string.ascii_letters + string.digits
	print(charset)

	for each_1 in charset:
		for each_2 in charset:
			key = each_1 + each_2

		ciphertext = "JHDFHDCYZJSQ"
		# print(f'CT:  {ciphertext}')

		# enciphered = vc.encipher(plaintext, keyword)
		# print(f'Enciphered: {enciphered}')

		deciphered = vc.decipher(ciphertext, key)
		
		if deciphered[1] == "R" or deciphered[1] == "r": 
			print(f'Deciphered: {deciphered}')




main()
