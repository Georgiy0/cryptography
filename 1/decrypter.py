import sys, os
import pickle
from BasicCrypto import *

def main(path):
	with open(path, "rb") as file:
		data = file.read()
	alphabet = pickle.load(open("alphabet.data", 'rb'))
	sc = ShiftCipher(alphabet, key)
	decrypted_data = sc.decrypt(data)
	with open("decrypted.data", 'wb') as file:
		file.write(decrypted_data)
	
	
if __name__ == "__main__":
	try:
		path = sys.argv[1]
		key = sys.argv[2]
	except:
		print("decrypter <file_path> <key>")
		exit(-1)
	if not os.path.isfile(path):
		print("Invalid path!")
		exit(-1)
	main(path)