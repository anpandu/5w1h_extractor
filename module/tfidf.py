# from dataprovider import MDP
import math

class TFIDF(object):

	def __init__(self):
		pass

	def freq(self, word, doc):
		return doc.count(word)
	 
	def word_count(self, doc):
		return len(doc)
	 
	def tf(self, word, doc):
		return (self.freq(word, doc) / float(self.word_count(doc)))
	 
	def num_docs_containing(self, word, list_of_docs):
		count = 0
		for document in list_of_docs:
			if self.freq(word, document) > 0:
				count += 1
		return 1 + count	 
	 
	def idf(self, word, list_of_docs):
		return math.log(len(list_of_docs) / float(self.num_docs_containing(word, list_of_docs)))

	def tf_idf(self, word, doc, list_of_docs):
		return (self.tf(word, doc) * self.idf(word, list_of_docs))	