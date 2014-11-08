from tokenizer import Tokenizer

class FeatureExtractor(object):

	def __init__(self):
		self.tokenizer = Tokenizer()
		pass

	def freq(self, word, doc):
		doc_tokens = self.tokenizer.getTokens(doc)
		word_tokens = self.tokenizer.getTokens(word)
		return len(self._getTokenIdx(word_tokens, doc_tokens))

	def prevToken(self, word, doc):
		doc_tokens = self.tokenizer.getTokens(doc)
		word_tokens = self.tokenizer.getTokens(word)
		idxs = self._getTokenIdx(word_tokens, doc_tokens)
		res = [doc_tokens[idx-1] if idx>0 else "_begin_" for idx in idxs]
		return res

	def nextToken(self, word, doc):
		doc_tokens = self.tokenizer.getTokens(doc)
		word_tokens = self.tokenizer.getTokens(word)
		idxs = self._getTokenIdx(word_tokens, doc_tokens)
		res = [doc_tokens[idx+len(word_tokens)] if idx<len(doc_tokens)-1 else "_end_" for idx in idxs]
		return res

	def _getTokenIdx(self, needles, hays):
		res = []
		for i, hay in enumerate(hays):
			if (needles==hays[i:i+len(needles)]):
				res.append(i)
		return res