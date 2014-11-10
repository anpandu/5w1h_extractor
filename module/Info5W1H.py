
from module.tokenizer import Tokenizer

class Info5W1H(object):

	def __init__(self, _what, _who, _when, _where, _why, _how, _text):
		self.tokenizer = Tokenizer()
		self.what = _what
		self.who = _who
		self.when = _when
		self.where = _where
		self.why = _why
		self.how = _how
		self.text = _text
		self.sentences = self.tokenizer.getSentences(_text)
		self.tokenized_sentences = [self.tokenizer.getTokens(sentence) for sentence in self.sentences]