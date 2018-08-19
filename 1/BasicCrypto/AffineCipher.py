from math import gcd

"""
Not optimized implementation of Euler function computation.
"""
def eulerFunction(n):
	result = 1
	for i in range(2, n):
		if gcd(n, i) == 1:
			result += 1
	return result

class AffineCipher:
	def __init__(self, alphabet, key_a, key_b):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		self.key_a, self.key_a_inverse, self.key_b = self.processKeys(key_a, key_b, self.modulo)
		self.alphabet_map = {}
		for i in range(0, self.modulo):
			self.alphabet_map[self.alphabet[i]] = i
		
	def processKeys(self, key_a, key_b, modulo):
		try:
			key_a = int(key_a)
			key_b = int(key_b)
		except:
			raise ValueError('Invalid key format')
		if gcd(key_a, modulo) != 1:
			raise ValueError('key_a should belong to multiplicative group Z_modulo')
		key_a %= modulo
		key_b %= modulo
		eulerFunc = eulerFunction(modulo)
		key_a_inverse = pow(key_a, eulerFunc - 1, modulo)
		return key_a, key_a_inverse, key_b
		
	def encrypt(self, data):
		encrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			encrypted_data += bytes([self.alphabet[(self.key_a * self.alphabet_map[byte] + self.key_b) % self.modulo]])
		return encrypted_data
			
	def decrypt(self, data):
		decrypted_data = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			decrypted_data += bytes([self.alphabet[(self.key_a_inverse * (self.alphabet_map[byte] - self.key_b)) % self.modulo]])
		return decrypted_data