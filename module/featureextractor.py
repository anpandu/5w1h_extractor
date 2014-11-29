from tokenizer import Tokenizer

class FeatureExtractor(object):

	@staticmethod
	def isIncludingString(string, word):
		return string in word

	@staticmethod
	def freq(word, doc):
		doc_tokens = Tokenizer.getTokens(doc)
		word_tokens = Tokenizer.getTokens(word)
		return len(FeatureExtractor._getTokenIdx(word_tokens, doc_tokens))

	@staticmethod
	def prevTokenInSentences(word, doc):
		sentences = Tokenizer.getSentences(doc)
		res = [prevtoken for sentence in sentences for prevtoken in FeatureExtractor.prevToken(word, sentence)]
		return res

	@staticmethod
	def nextTokenInSentences(word, doc):
		sentences = Tokenizer.getSentences(doc)
		res = [nexttoken for sentence in sentences for nexttoken in FeatureExtractor.nextToken(word, sentence)]
		return res

	@staticmethod
	def prevToken(word, doc):
		doc_tokens = Tokenizer.getTokens(doc)
		word_tokens = Tokenizer.getTokens(word)
		idxs = FeatureExtractor._getTokenIdx(word_tokens, doc_tokens)
		res = [doc_tokens[idx-1] if idx>0 else "_begin_" for idx in idxs]
		return res

	@staticmethod
	def nextToken(word, doc):
		doc_tokens = Tokenizer.getTokens(doc)
		word_tokens = Tokenizer.getTokens(word)
		idxs = FeatureExtractor._getTokenIdx(word_tokens, doc_tokens)
		res = [doc_tokens[idx+len(word_tokens)] if idx<len(doc_tokens)-len(word_tokens) else "_end_" for idx in idxs]
		return res

	@staticmethod
	def _getTokenIdx(needles, hays):
		if (len(needles)>0):
			res = []
			for i, hay in enumerate(hays):
				if (needles==hays[i:i+len(needles)]):
					res.append(i)
			return res
		else:
			return []