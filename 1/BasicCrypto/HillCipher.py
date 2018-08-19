from math import gcd
from Helper import eulerFunction

"""
Implements Hill Cipher with the 2x2 matrix key.
If the length of the data is odd then the last byte of data is not encrypted.
"""
class HillCipher:
	def __init__(self, alphabet, key):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		self.key, self.key_inverse = self.processKey(key, self.modulo)
		self.alphabet_map = {}
		for i in range(0, self.modulo):
			self.alphabet_map[self.alphabet[i]] = i
		
	def processKey(self, key, modulo):
		if not isinstance(key, list):
			raise ValueError('Invalid key provided')
		else:
			det = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % modulo
			if gcd(det, modulo) != 1:
				raise ValueError('gcd(det, modulo) != 1')
			det_inverse = pow(det, eulerFunction(modulo) - 1, modulo)
			key_inverse = [[key[1][1]*det_inverse, (modulo - key[0][1])*det_inverse],[(modulo - key[1][0])*det_inverse, key[0][0] * det_inverse]]
			return key, key_inverse
			
	def encrypt(self, data):
		last_byte = None
		if len(data) % 2 != 0:
			last_byte = data[len(data) - 1]
			data = data[:-1]
		encrypted_data = b''
		for i in range(0, len(data), 2):
			if data[i] not in self.alphabet or data[i + 1] not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			x = self.alphabet_map[data[i]]
			y = self.alphabet_map[data[i + 1]]
			encrypted_data += bytes([self.alphabet[(x*self.key[0][0] + y*self.key[1][0]) % self.modulo], self.alphabet[(x*self.key[0][1] + y*self.key[1][1]) % self.modulo]])
		if last_byte != None:
			encrypted_data += bytes([last_byte])
		return encrypted_data
			
	def decrypt(self, data):
		last_byte = None
		if len(data) % 2 != 0:
			last_byte = data[len(data) - 1]
			data = data[:-1]
		decrypted_data = b''
		for i in range(0, len(data), 2):
			if data[i] not in self.alphabet or data[i + 1] not in self.alphabet:
				raise ValueError("Alphabet of the data doesn't match with the provided alphabet")
			x = self.alphabet_map[data[i]]
			y = self.alphabet_map[data[i + 1]]
			decrypted_data += bytes([self.alphabet[(x*self.key_inverse[0][0] + y*self.key_inverse[1][0]) % self.modulo], self.alphabet[(x*self.key_inverse[0][1] + y*self.key_inverse[1][1]) % self.modulo]])
		if last_byte != None:
			decrypted_data += bytes([last_byte])
		return decrypted_data