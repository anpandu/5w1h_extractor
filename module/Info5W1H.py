from tokenizer import Tokenizer

class Info5W1H(object):

	def __init__(self, _what, _who, _when, _where, _why, _how, _text):
		self.what = Tokenizer.removeNonAscii(_what).replace(".\"",". \"")
		self.who = Tokenizer.removeNonAscii(_who).replace(".\"",". \"")
		self.when = Tokenizer.removeNonAscii(_when).replace(".\"",". \"")
		self.where = Tokenizer.removeNonAscii(_where).replace(".\"",". \"")
		self.why = Tokenizer.removeNonAscii(_why).replace(".\"",". \"")
		self.how = Tokenizer.removeNonAscii(_how).replace(".\"",". \"")
		self.text = Tokenizer.removeNonAscii(_text).replace(".\"",". \"")
		self.sentences = Tokenizer.getSentences(self.text)
		self.tokenized_sentences = [Tokenizer.getTokens(sentence) for sentence in self.sentences]