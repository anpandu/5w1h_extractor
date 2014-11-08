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