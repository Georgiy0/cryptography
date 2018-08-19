class ShiftCipher:
	def __init__(self, alphabet, key):
		self.key = self.processKey(key)
		self.alphabet = alphabet
		if self.key not in self.alphabet:
			raise ValueError('Provided key does not belong to the alphabet')
		self.modulo = len(alphabet)
		self.alphabet_map = {}
		for i in range(0, self.modulo):
			self.alphabet_map[self.alphabet[i]] = i
		self.key_pos = self.alphabet_map[self.key]
		
	def processKey(self, key):
		if isinstance(key, int):
			return key
		elif isinstance(key, str):
			if len(key) != 1:
				raise ValueError('Invalid key provided')
			else:
				return ord(key[0])
		else:
			raise ValueError('Invalid key provided')
		
	def encrypt(self, data):
		encrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			encrypted_data += bytes([self.alphabet[(self.alphabet_map[byte] + self.key_pos) % self.modulo]])
		return encrypted_data
			
	def decrypt(self, data):
		decrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			decrypted_data += bytes([self.alphabet[(self.alphabet_map[byte] - self.key_pos) % self.modulo]])
		return decrypted_data