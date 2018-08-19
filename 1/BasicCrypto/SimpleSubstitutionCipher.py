from random import randint

class SimpleSubstitutionCipher:
	def __init__(self, alphabet, key=None):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		if key == None:
			self.key = self.generateKey(self.alphabet, self.modulo)
		else:
			self.key = self.processKey(key)
		self.inverse_key = {}
		for index in self.key:
			self.inverse_key[self.key[index]] = index
		
	def generateKey(self, alphabet, modulo):
		alphabet_indexes = list(range(modulo))
		key = {}
		for i in range(modulo):
			key[alphabet[i]] = alphabet[alphabet_indexes.pop(randint(0, len(alphabet_indexes) - 1))]
		return key
		
	def processKey(self, key):
		if not isinstance(key, dict):
			raise ValueError('Invalid key provided')
		else:
			return key
		
	def encrypt(self, data):
		encrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			encrypted_data += bytes([self.key[byte]])
		return encrypted_data
			
	def decrypt(self, data):
		decrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			decrypted_data += bytes([self.inverse_key[byte]])
		return decrypted_data