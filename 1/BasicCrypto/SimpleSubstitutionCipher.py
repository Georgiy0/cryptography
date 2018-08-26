from random import randint
from ShiftCipher import ShiftCipher

class SimpleSubstitutionCipher(ShiftCipher):
	def __init__(self, alphabet, key=None):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		if key == None:
			self.key = self.generateKey()
		else:
			self.key = self.processKey(key)
		self.inverse_key = {}
		for index in self.key:
			self.inverse_key[self.key[index]] = index
		
	def generateKey(self):
		alphabet_indexes = list(range(self.modulo))
		key = {}
		for i in range(self.modulo):
			key[self.alphabet[i]] = self.alphabet[alphabet_indexes.pop(randint(0, len(alphabet_indexes) - 1))]
		return key
		
	def processKey(self, key):
		if not isinstance(key, dict):
			raise ValueError('Invalid key provided')
		else:
			for index in key:
				if index not in self.alphabet or key[index] not in self.alphabet:
					raise ValueError('Alphabets do not match')
			return key
			
	def encryptByte(self, byte):
		return bytes([self.key[byte]])
		
	def decryptByte(self, byte):
		return bytes([self.inverse_key[byte]])