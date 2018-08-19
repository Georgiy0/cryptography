import sys, os
import pickle
from BasicCrypto import *

def main(path, key):
	with open(path, "rb") as file:
		data = file.read()
	frequencies = {}
	alphabet = []
	for byte in data:	
		if byte not in alphabet:
			alphabet.append(byte)
			frequencies[byte] = 1
		else:
			frequencies[byte] += 1
	alphabet.sort()
	pickle.dump(alphabet, open("alphabet.data", 'wb'))
	pickle.dump(frequencies, open("frequencies.data", 'wb'))
	cipher = HillCipher(alphabet, key)
	encrypted_data = cipher.encrypt(data)
	with open("encrypted.data", 'wb') as file:
		file.write(encrypted_data)
	
if __name__ == "__main__":
	try:
		path = sys.argv[1]
		key = [[int(sys.argv[2]), int(sys.argv[3])],[int(sys.argv[4]), int(sys.argv[5])]]
	except:
		print("encrypter <file_path> <key_matrix_2x2>")
		exit(-1)
	if not os.path.isfile(path):
		print("Invalid path!")
		exit(-1)
	main(path, key)