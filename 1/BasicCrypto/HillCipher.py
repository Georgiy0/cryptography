from math import gcd
from Helper import eulerFunction
from BlockCipher import BlockCipher

"""
Implements Hill Cipher with the 2x2 matrix key.
If the length of the data is odd then the last byte of data is not encrypted.
"""
class HillCipher:
	def __init__(self, alphabet, key):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		self.key = self.processKey(key)
		self.blockSize = 2
		self.alphabet_map = {}
		for i in range(0, self.modulo):
			self.alphabet_map[self.alphabet[i]] = i
		
	def processKey(self, key):
		if not isinstance(key, list):
			raise ValueError('Invalid key provided')
		else:
			det = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % modulo
			if gcd(det, self.modulo) != 1:
				raise ValueError('gcd(det, self.modulo) != 1')
			det_inverse = pow(det, eulerFunction(self.modulo) - 1, self.modulo)
			key_inverse = [[key[1][1]*det_inverse, (self.modulo - key[0][1])*det_inverse],[(self.modulo - key[1][0])*det_inverse, key[0][0] * det_inverse]]
			return (key, key_inverse)
			
	def encryptBlock(self, block):
		x = block[0]
		y = block[1]
		key = self.key[0]
		return bytes([self.alphabet[(x*key[0][0] + y*key[1][0]) % self.modulo], self.alphabet[(x*key[0][1] + y*key[1][1]) % self.modulo]])
		
	def decryptBlock(self, block):
		x = block[0]
		y = block[1]
		key_inverse = self.key[1]
		return bytes([self.alphabet[(x*key_inverse[0][0] + y*key_inverse[1][0]) % self.modulo], self.alphabet[(x*key_inverse[0][1] + y*key_inverse[1][1]) % self.modulo]])