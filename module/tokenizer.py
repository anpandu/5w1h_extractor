from nltk.tokenize import word_tokenize
import re


class Tokenizer(object):

	def __init__(self):
		self.stopwords = ['dan', 'atau', 'tetapi', 'tapi', 'akan tetapi', 'jika', 'kalau', 'karena', 'walau', 'walaupun', 'juga', 'jadi', 'maka', 'sehingga', 'supaya', 'agar', 'hanya', 'lagi', 'lagipula', 'lalu', 'sambil', 'melainkan', 'namun', 'padahal', 'sedangkan', 'demi', 'untuk', 'apabila', 'sebab', 'asalkan', 'meskipun', 'biarpun', 'biar', 'seperti', 'daripada', 'bahkan', 'apalagi', 'yakni', 'adalah', 'yaitu', 'ialah', 'bahwa', 'kecuali', 'selain', 'misalnya', 'itu', 'di', 'yang', 'dengan', 'ke', 'anda', 'sangat', 'ini', 'dari']

	def tokenize(self, str):
		# is string
		res = str
		res = self.removeNonAscii(res)
		res = self.toLowercase(res)
		res = self.spaceCorrect(res)
		res = word_tokenize(res) # !!! :
		# is list
		res = self.removeSymbol(res)
		res = self.stripSymbol(res)
		res = self.removeDigit(res)
		res = self.removeStopWords(res, self.stopwords)
		return res

	def tokenizeWithStopwords(self, str):
		# is string
		res = str
		res = self.removeNonAscii(res)
		res = self.toLowercase(res)
		res = self.spaceCorrect(res)
		res = word_tokenize(res) # !!! :
		# is list
		res = self.removeSymbol(res)
		res = self.stripSymbol(res)
		res = self.removeDigit(res)
		return res

	def removeStopWords(self, words, stopwords):
		res = [word for word in words if word not in stopwords]
		return res

	def toLowercase(self, str):
		return str.lower()

	def spaceCorrect(self, str):
		return str.replace('jt', ' jt').replace('m2', ' m2').replace('juta', ' juta').replace('rp', ' rp ').replace('0m', '0 m').replace('0rb', ' rb ')

	def removeDigit(self, arr):
		res = arr
		removed_chars = [".", ",", "-", "x", "+", "/", "lt", "lb", "km", "kt", ":"]
		for rc in removed_chars:
			res = [item for item in res if (self._removeDigit(item).isdigit()==0)]
		return res

	def _removeDigit(self, str):
		res = str
		removed_chars = [".", ",", "-", "x", "+", "/", "lt", "lb", "km", "kt", ":"]
		for rc in removed_chars:
			res = res.replace(rc, "")
		return res

	def removeSymbol(self, arr):
		res = arr
		removed_chars = [
			"(", ")", "<", ">", 
			"/", "\\", 
			".", ",", ";", "|", "?", 
			":", "=", 
			"!", "@", "#", "$", "%", "&", "*", "-", "+"
		]
		for rc in removed_chars:
			res = [item for item in res if item != rc]
		return res

	def stripSymbol(self, arr):
		res = arr
		removed_chars = [
			"(", ")", "<", ">", 
			"/", "\\", 
			".", ",", ";", "|", "?", 
			":", "=", 
			"!", "@", "#", "$", "%", "&", "*", "-", "+"
		]
		for rc in removed_chars:
			res = [item.strip(rc) for item in res]
		return res

	def removeNonAscii(self, str):
		return ''.join([i if ord(i) < 128 else ' ' for i in str])