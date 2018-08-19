import sys, os
import pickle
from BasicCrypto import *

def main(path, key_path):
	with open(path, "rb") as file:
		data = file.read()
	alphabet = pickle.load(open("alphabet.data", 'rb'))
	key = pickle.load(open("ssc.key", 'rb'))
	cipher = SimpleSubstitutionCipher(alphabet, key)
	decrypted_data = cipher.decrypt(data)
	with open("decrypted.data", 'wb') as file:
		file.write(decrypted_data)
	
if __name__ == "__main__":
	try:
		path = sys.argv[1]
		key_path = sys.argv[2]
	except:
		print("decrypter <file_path> <key_file_path>")
		exit(-1)
	if not os.path.isfile(path) or not os.path.isfile(key_path):
		print("Invalid path!")
		exit(-1)
	main(path, key_path)