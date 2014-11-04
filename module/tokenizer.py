import re


class Tokenizer(object):

	def __init__(self):
		self.entityjoin = ['dan', 'untuk']
		self.entityjoinexception = ['Rp']

	def getTokens(self, str): # !!! kata 'dan' pas terakhir
		rawtokens = str.split(' ')		
		# split non-alnum first char of token
		again = True
		while again:
			rawtokens2 = []
			for i, rawtoken in enumerate(rawtokens):
				if (not rawtoken[0].isalnum() and len(rawtoken)>1):
					rawtokens2.append(rawtoken[0])
					rawtokens2.append(rawtoken[1:])
				else: 
					rawtokens2.append(rawtoken)
			rawtokens = rawtokens2
			again = False
			for i, rawtoken in enumerate(rawtokens):
				again = again or (not rawtoken[0].isalnum() and len(rawtoken)>1)
		# split non-alnum last char of token
		again = True
		while again:
			rawtokens2 = []
			for i, rawtoken in enumerate(rawtokens):
				if (not rawtoken[-1].isalnum() and len(rawtoken)>1):
					rawtokens2.append(rawtoken[:-1])
					rawtokens2.append(rawtoken[-1])
				else: 
					rawtokens2.append(rawtoken)
			rawtokens = rawtokens2
			again = False
			for i, rawtoken in enumerate(rawtokens):
				again = again or (not rawtoken[-1].isalnum() and len(rawtoken)>1)
		return rawtokens

	def getTerms(self, str): # !!! kata 'dan' pas terakhir
		rawtokens = self.getTokens(str)
		terms = []
		temp = []
		for rawtoken in rawtokens:
			if ((rawtoken[0].isupper() or (rawtoken in self.entityjoin)) and (rawtoken not in self.entityjoinexception)):
				temp.append(rawtoken)
			elif (len(temp)>0):
				terms.append(' '.join(temp))
				temp = []
				terms.append(rawtoken)
			else: 
				terms.append(rawtoken)
		return terms

	def getSentenceFromText(self, str):
		res = str.split('. ')
		res = [item.split(' - ') for item in res]
		res = [item for sublist in res for item in sublist]
		return res

	def removeNonAscii(self, str):
		return ''.join([i if ord(i) < 128 else ' ' for i in str])