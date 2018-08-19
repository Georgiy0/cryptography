import sys, os
import pickle
from BasicCrypto import *

def main(path, key_a, key_b):
	with open(path, "rb") as file:
		data = file.read()
	alphabet = pickle.load(open("alphabet.data", 'rb'))
	cipher = AffineCipher(alphabet, key_a, key_b)
	decrypted_data = cipher.decrypt(data)
	with open("decrypted.data", 'wb') as file:
		file.write(decrypted_data)
	
if __name__ == "__main__":
	try:
		path = sys.argv[1]
		key_a = sys.argv[2]
		key_b = sys.argv[3]
	except:
		print("decrypter <file_path> <key_a> <key_b>")
		exit(-1)
	if not os.path.isfile(path):
		print("Invalid path!")
		exit(-1)
	main(path, key_a, key_b)