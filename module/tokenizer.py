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
				if len(rawtoken)>1:
					if (not rawtoken[0].isalnum()):
						rawtokens2.append(rawtoken[0])
						rawtokens2.append(rawtoken[1:])
					else: 
						rawtokens2.append(rawtoken)
				else:
					rawtokens2.append(rawtoken)
			rawtokens = rawtokens2
			again = False
			for i, rawtoken in enumerate(rawtokens):
				if len(rawtoken)>1:
					again = again or (not rawtoken[0].isalnum())
		# split non-alnum last char of token
		again = True
		while again:
			rawtokens2 = []
			for i, rawtoken in enumerate(rawtokens):
				if len(rawtoken)>1:
					if (not rawtoken[-1].isalnum()):
						rawtokens2.append(rawtoken[:-1])
						rawtokens2.append(rawtoken[-1])
					else: 
						rawtokens2.append(rawtoken)
				else:
					rawtokens2.append(rawtoken)
			rawtokens = rawtokens2
			again = False
			for i, rawtoken in enumerate(rawtokens):
				if len(rawtoken)>1:
					again = again or (not rawtoken[-1].isalnum())
		return rawtokens

	def getTerms(self, str): # !!! kata 'dan' pas terakhir
		tokens = self.getTokens(str)
		terms = []
		temp = []
		for token in tokens:
			if ((token[0].isupper()) and (token not in self.entityjoinexception)):
				temp.append(token)
			elif (len(temp)>0):
				terms.append(' '.join(temp))
				temp = []
				terms.append(token)
			else: 
				terms.append(token)
		return terms

	def getSentences(self, str):
		res = str.split('. ')
		res = [item.split(' - ') for item in res]
		res = [item for sublist in res for item in sublist]
		res = [item for item in res if item is not ''] #remove null
		# remove dot in last char of last sentence
		last_sentence = res[len(res)-1]
		res[len(res)-1] = last_sentence[:-1] if (last_sentence[-1]=='.') else last_sentence
		return res

	def removeNonAscii(self, str):
		return ''.join([i if ord(i) < 128 else ' ' for i in str])