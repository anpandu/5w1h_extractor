import re


class Tokenizer(object):

	entityjoin = ['dan', 'untuk']
	entityjoinexception = ['Rp']

	@staticmethod
	def getTokens(str): # !!! kata 'dan' pas terakhir
		# bersih2
		str = str.replace(',"', ', "')
		str = str.replace('"-', '" -')
		#
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
		rawtokens = [rawtoken for rawtoken in rawtokens if rawtoken!='']
		return rawtokens

	@staticmethod
	def getNTokens(str, n): # sliding window
		tokens = Tokenizer.getTokens(str)
		res = []
		for i in range(0,n):
			for j in range(0, len(tokens)-i):
				temp = []
				for k in range(0,i+1):
					if (j+k<len(tokens)):
						temp.append(tokens[j+k])
				res.append(" ".join(temp))
		return res

	@staticmethod
	def getTerms(str): # !!! kata 'dan' pas terakhir
		tokens = Tokenizer.getTokens(str)
		terms = []
		temp = []
		for token in tokens:
			if ((token[0].isupper()) and (token not in Tokenizer.entityjoinexception)):
				temp.append(token)
			elif (len(temp)>0):
				terms.append(' '.join(temp))
				temp = []
				terms.append(token)
			else: 
				terms.append(token)
		return terms

	@staticmethod
	def getSentences(str):
		res = str.split('. ')
		res = [item.split(' - ') for item in res]
		res = [item for sublist in res for item in sublist]
		res = [item for item in res if item is not ''] #remove null
		res = [sen+'.' for sen in res]
		# remove dot in last char of last sentence
		last_sentence = res[len(res)-1]
		res[len(res)-1] = last_sentence[:-1] if (last_sentence[-1]=='.') else last_sentence
		return res

	@staticmethod
	def removeNonAscii(stri):
		return "".join([ch for ch in stri if ord(ch)< 127 and ord(ch)> 31 ])