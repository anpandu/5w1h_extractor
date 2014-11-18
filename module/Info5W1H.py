
from tokenizer import Tokenizer

class Info5W1H(object):

	def __init__(self, _what, _who, _when, _where, _why, _how, _text):
		self.tokenizer = Tokenizer()
		self.what = self.tokenizer.removeNonAscii(_what)
		self.who = self.tokenizer.removeNonAscii(_who)
		self.when = self.tokenizer.removeNonAscii(_when)
		self.where = self.tokenizer.removeNonAscii(_where)
		self.why = self.tokenizer.removeNonAscii(_why)
		self.how = self.tokenizer.removeNonAscii(_how)
		self.text = self.tokenizer.removeNonAscii(_text)
		self.sentences = self.tokenizer.getSentences(self.text)
		self.tokenized_sentences = [self.tokenizer.getTokens(sentence) for sentence in self.sentences]