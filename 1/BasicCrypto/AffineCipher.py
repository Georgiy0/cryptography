from math import gcd
from Helper import eulerFunction
from ShiftCipher import ShiftCipher

class AffineCipher(ShiftCipher):
	def processKey(self, key):
		try:
			key_a = int(key[0])
			key_b = int(key[1])
		except:
			raise ValueError('Invalid key format')
		if gcd(key_a, self.modulo) != 1:
			raise ValueError('key_a should belong to multiplicative group Z_modulo')
		key_a %= self.modulo
		key_b %= self.modulo
		key_a_inverse = pow(key_a, eulerFunction(self.modulo) - 1, self.modulo)
		return (key_a, key_b, key_a_inverse)
		
	def generateKey(self):
		raise NotImplementedError('Key generation not implemented')
		
	def encryptByte(self, byte):
		key_a, key_b = self.key[0], self.key[1]
		return bytes([self.alphabet[(key_a * self.alphabet_map[byte] + key_b) % self.modulo]])
		
	def decryptByte(self, byte):
		key_a, key_b, key_a_inverse = self.key[0], self.key[1], self.key[2]
		return bytes([self.alphabet[(key_a_inverse * (self.alphabet_map[byte] - key_b)) % self.modulo]])