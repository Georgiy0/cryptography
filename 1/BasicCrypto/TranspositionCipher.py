from random import randint
from BlockCipher import BlockCipher

"""
Implements transposition cipher with the blocks of provided length (by default blockSize is 8 byte).
If the data cannot be devided in final number of length the last incomplete block won't be encrypted.
"""
class TranspositionCipher(BlockCipher):
	def __init__(self, alphabet, key=None, blockSize=None):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		if key == None:
			self.key = self.generateKey(blockSize)
		else:
			self.key = self.processKey(key)
		self.key_inverse = {}
		for index in self.key:
			self.key_inverse[self.key[index]] = index
		self.blockSize = len(self.key)
		
	def processKey(self, key):
		if not isinstance(key, dict):
			raise ValueError('Invalid key format')
		return key
		
	def generateKey(self, blockSize):
		if blockSize == None:
			blockSize = 8
		indexes = list(range(blockSize))
		key = {}
		for i in range(0, blockSize):
			key[i] = indexes.pop(randint(0, len(indexes) - 1))
		return key
		
	def encryptBlock(self, block):
		encrypted_block = b''
		for block_i in range(0, self.blockSize):
			encrypted_block += bytes([block[self.key[block_i]]])
		return encrypted_block
		
	def decryptBlock(self, block):
		decrypted_block = b''
		for block_i in range(0, self.blockSize):
			decrypted_block += bytes([block[self.key_inverse[block_i]]])
		return decrypted_block