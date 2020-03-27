#
# Akhil Kumar
# akhil.kumar_ug21@ashoka.edu.in
# CS-2362 Computer Security and Privacy
# RSA driver code
#

import keygen, encrypt, decrypt

def main():
	print ("Generating keys ...")
	if (keygen.makeKeys()):
		print ("Key generation failed!")
		return 1

	print ("Encrypting plaintext ...")
	if (encrypt.encrypt()):
		print ("Encryption failed!")
		return 2

	print ("Decrypting plaintext ...")
	if (decrypt.decrypt()):
		print ("Decryption failed!")
		return 3

main()	