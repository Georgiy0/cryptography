from BaseCipher import BaseCipher
from random import randint

class ShiftCipher(BaseCipher):
	def __init__(self, alphabet, key=None):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		if key != None:
			self.key = self.processKey(key)
		else:
			self.key = self.generateKey()
		self.buildAlphabetMap()
		
	def buildAlphabetMap(self):
		self.alphabet_map = {}
		for i in range(0, self.modulo):
			self.alphabet_map[self.alphabet[i]] = i
		
	def processKey(self, key):
		if isinstance(key, int):
			return key
		elif isinstance(key, str):
			try:
				return int(key) & self.modulo
			except:
				raise ValueError('Invalid key provided')
		else:
			raise ValueError('Invalid key provided')
			
	def generateKey(self):
		self.key = randint(0, modulo - 1)
				
	def transformData(self, data, transformation):
		newData = b''
		for byte in data:
			if byte not in self.alphabet:
				raise ValueError("Alphabets do not match")
			newData += transformation(byte)
		return newData
		
	def encryptByte(self, byte):
		return bytes([self.alphabet[(self.alphabet_map[byte] + self.key) % self.modulo]])
		
	def encrypt(self, data):
		return self.transformData(data, self.encryptByte)
	
	def decryptByte(self, byte):
		return bytes([self.alphabet[(self.alphabet_map[byte] - self.key) % self.modulo]])
			
	def decrypt(self, data):
		return self.transformData(data, self.decryptByte)