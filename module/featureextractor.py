from tokenizer import Tokenizer

class FeatureExtractor(object):

	def __init__(self):
		self.tokenizer = Tokenizer()
		pass

	def freq(self, word, doc):
		doc_tokens = self.tokenizer.getTokens(doc)
		res = 0
		for doc_token in doc_tokens:
			res += 1 if (doc_token==word) else 0
		return res

	def prevToken(self, word, doc):
		doc_tokens = self.tokenizer.getTokens(doc)
		res = []
		for i, doc_token in enumerate(doc_tokens):
			if (doc_token==word and i>0):
				res.append(doc_tokens[i-1])
		return res

	def nextToken(self, word, doc):
		doc_tokens = self.tokenizer.getTokens(doc)
		limit = len(doc_tokens)
		res = []
		for i, doc_token in enumerate(doc_tokens):
			if (doc_token==word and i<limit-1):
				res.append(doc_tokens[i+1])
		return res

