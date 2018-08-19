import sys, os
import pickle
from BasicCrypto import *

def main(path, key):
	with open(path, "rb") as file:
		data = file.read()
	alphabet = pickle.load(open("alphabet.data", 'rb'))
	cipher = HillCipher(alphabet, key)
	decrypted_data = cipher.decrypt(data)
	with open("decrypted.data", 'wb') as file:
		file.write(decrypted_data)
	
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