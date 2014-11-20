from tokenizer import Tokenizer

class Info5W1H(object):

	def __init__(self, _what, _who, _when, _where, _why, _how, _text):
		self.what = Tokenizer.removeNonAscii(_what)
		self.who = Tokenizer.removeNonAscii(_who)
		self.when = Tokenizer.removeNonAscii(_when)
		self.where = Tokenizer.removeNonAscii(_where)
		self.why = Tokenizer.removeNonAscii(_why)
		self.how = Tokenizer.removeNonAscii(_how)
		self.text = Tokenizer.removeNonAscii(_text)
		self.sentences = Tokenizer.getSentences(self.text)
		self.tokenized_sentences = [Tokenizer.getTokens(sentence) for sentence in self.sentences]