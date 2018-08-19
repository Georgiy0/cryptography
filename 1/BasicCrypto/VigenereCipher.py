class VigenereCipher:
	def __init__(self, alphabet, key):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		self.key = self.processKey(key)
		self.alphabet_map = {}
		for i in range(0, self.modulo):
			self.alphabet_map[self.alphabet[i]] = i
		
	def processKey(self, key):
		key = key.encode('ascii')
		for byte in key:
			if byte not in self.alphabet:
				raise ValueError('Invalid key format')
		return key
		
	def encrypt(self, data):
		encrypted_data = b''
		key_index = 0
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			encrypted_data += bytes([self.alphabet[(self.alphabet_map[byte] + self.alphabet_map[self.key[key_index]]) % self.modulo]])
			key_index = (key_index + 1) % len(self.key)
		return encrypted_data
			
	def decrypt(self, data):
		decrypted_data = b''
		key_index = 0
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			decrypted_data += bytes([self.alphabet[(self.alphabet_map[byte] - self.alphabet_map[self.key[key_index]]) % self.modulo]])
			key_index = (key_index + 1) % len(self.key)
		return decrypted_data