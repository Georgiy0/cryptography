from abc import ABC, abstractmethod

class BaseCipher(ABC):
	@abstractmethod
	def processKey(self, key):
		pass
		
	@abstractmethod
	def generateKey(self):
		pass
	
	@abstractmethod
	def encrypt(self, data):
		pass
	
	@abstractmethod
	def decrypt(self, data):
		pass