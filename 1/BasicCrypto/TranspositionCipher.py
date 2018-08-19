from random import randint

"""
Implements transposition cipher with the blocks of provided length (by default block_size is 8 byte).
If the data cannot be devided in final number of length the last incomplete block won't be encrypted.
"""
class TranspositionCipher:
	def __init__(self, alphabet, key=None, block_size=None):
		self.alphabet = alphabet
		self.modulo = len(alphabet)
		if key == None:
			self.key = self.generateKey(block_size)
		else:
			self.key = self.processKey(key)
		self.key_inverse = {}
		for index in self.key:
			self.key_inverse[self.key[index]] = index
		self.block_size = len(self.key)
		
	def processKey(self, key):
		if not isinstance(key, dict):
			raise ValueError('Invalid key format')
		return key
		
	def generateKey(self, block_size):
		if block_size == None:
			block_size = 8
		indexes = list(range(block_size))
		key = {}
		for i in range(0, block_size):
			key[i] = indexes.pop(randint(0, len(indexes) - 1))
		return key
		
	def encrypt(self, data):
		last_bytes = None
		if len(data) % self.block_size != 0:
			last_bytes = data[len(data) - len(data) % self.block_size:]
			data = data[:-(len(data) % self.block_size)]
		encrypted_data = b''
		for i in range(0, len(data), self.block_size):
			block = data[i:i + self.block_size]
			encrypted_block = b''
			for block_i in range(0, self.block_size):
				encrypted_block += bytes([block[self.key[block_i]]])
			encrypted_data += encrypted_block
		if last_bytes != None:
			encrypted_data += last_bytes
		return encrypted_data
			
	def decrypt(self, data):
		last_bytes = None
		if len(data) % self.block_size != 0:
			last_bytes = data[len(data) - len(data) % self.block_size:]
			data = data[:-(len(data) % self.block_size)]
		decrypted_data = b''
		for i in range(0, len(data), self.block_size):
			block = data[i:i + self.block_size]
			decrypted_block = b''
			for block_i in range(0, self.block_size):
				decrypted_block += bytes([block[self.key_inverse[block_i]]])
			decrypted_data += decrypted_block
		if last_bytes != None:
			decrypted_data += last_bytes
		return decrypted_data