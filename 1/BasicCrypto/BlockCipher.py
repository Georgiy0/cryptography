from abc import ABC, abstractmethod
from BaseCipher import BaseCipher

class BlockCipher(BaseCipher):	
	def addPadding(self, data):
		n = len(data) % self.blockSize
		if n != 0:
			n = self.blockSize - n
			data += bytes([n]*n)
			if n not in self.alphabet:
				self.alphabet.append(n)
				self.alphabet.sort()
		return data
		
	def deletePadding(self, data):
		if len(data) < self.blockSize:
			raise ValueError('Data length is less than blockSize')
		index = len(data) - 1
		i = self.blockSize
		paddingByte = data[index]
		cnt = 0
		while i and data[index] == paddingByte:
			cnt += 1
			i -= 1
			index -= 1
		if cnt == paddingByte:
			data = data[:-cnt]
		return data
		
	def transformData(self, data, transformation):
		newData = b''
		for i in range(0, len(data), self.blockSize):
			newData += transformation(data[i:i + self.blockSize])
		return newData
		
	@abstractmethod
	def encryptBlock(self, block):
		pass
		
	def encrypt(self, data):
		return self.transformData(self.addPadding(data), self.encryptBlock)
		
	@abstractmethod
	def decryptBlock(self, block):
		pass
			
	def decrypt(self, data):
		return self.deletePadding(self.transformData(data, self.decryptBlock))
		