#
# Akhil Kumar
# akhil.kumar_ug21@ashoka.edu.in
# CS-2362 Computer Security and Privacy
# RSA Decrypt
#

import helper

#
# Decrypt a message using private key 
# (and public modulus)
#
def decrypt():
	# open ciphertext
	fo = open("ciphertext.txt", "r")
	c = fo.read().rstrip('\n')
	ciphertext = int(c)
	fo.close()

	# Extract our Public key of the form (e, n)
	PublicKey = tuple(open("public_key.txt", "r"))
	key = int(PublicKey[0])
	n = int(PublicKey[1])

	# Extract private key
	fo = open("private_key.txt", "r")
	p = fo.read().rstrip('\n')
	PrivateKey = int(p)
	fo.close()

	# Decrypt ciphertext using formula
	# m = c^d mod n
	d = (helper.modexp(ciphertext, PrivateKey, n))

	size = int(helper.keysize/8)

	fo = open("deciphertext.txt", "w")
	fo.write(str(d.to_bytes(size, byteorder = 'big'), 'utf-8').rstrip('\n'))
	fo.close()

	return 0
	
decrypt()
