class ShiftCipher:
	def __init__(self, alphabet, key):
		self.key = self.processKey(key)
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		self.key %= modulo
		self.alphabet_map = {}
		for i in range(0, self.modulo):
			self.alphabet_map[self.alphabet[i]] = i
		
	def processKey(self, key):
		if isinstance(key, int):
			return key
		elif isinstance(key, str):
			try:
				return int(key)
			except:
				raise ValueError('Invalid key provided')
		else:
			raise ValueError('Invalid key provided')
		
	def encrypt(self, data):
		encrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			encrypted_data += bytes([self.alphabet[(self.alphabet_map[byte] + self.key) % self.modulo]])
		return encrypted_data
			
	def decrypt(self, data):
		decrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			decrypted_data += bytes([self.alphabet[(self.alphabet_map[byte] - self.key) % self.modulo]])
		return decrypted_data