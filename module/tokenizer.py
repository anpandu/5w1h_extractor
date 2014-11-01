from nltk.tokenize import word_tokenize
import re


class Tokenizer(object):

	def __init__(self):
		self.entityjoin = ['dan', 'untuk']
		self.entityjoinexception = ['Rp']

	def tokenize(self, str):
		res = word_tokenize(str) # !!! :
		return res

	def tokenize2(self, str): # !!! kata 'dan' pas terakhir
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

		# join uppercased words to one word/token
		tokens = []
		temp = []
		for rawtoken in rawtokens:
			if ((rawtoken[0].isupper() or (rawtoken in self.entityjoin)) and (rawtoken not in self.entityjoinexception)):
				temp.append(rawtoken)
			elif (len(temp)>0):
				tokens.append(' '.join(temp))
				temp = []
				tokens.append(rawtoken)
			else: 
				tokens.append(rawtoken)
		return tokens

	def getSentenceFromText(self, str):
		res = str.split('. ')
		res = [item.split(' - ') for item in res]
		res = [item for sublist in res for item in sublist]
		return res

	def removeNonAscii(self, str):
		return ''.join([i if ord(i) < 128 else ' ' for i in str])