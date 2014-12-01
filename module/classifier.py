import nltk
import pickle
from module.tokenizer import Tokenizer
from module.fe.fe_when import FeatureExtractorWhen

class Classifier(object):

	@staticmethod
	def trainWhen(info5w1hs):
		fiturs = []
		for info in info5w1hs:
			for token in Tokenizer.getNTokens(info.text, 5):
				fiturs.append( (FeatureExtractorWhen.getFeatureWhen(token, info.text), Tokenizer.getTokens(token)==Tokenizer.getTokens(info.when)) )
		c = nltk.NaiveBayesClassifier.train(fiturs)
		return {"classifier": c, "fiturs": fiturs}

	@staticmethod
	def saveClassifier(c, filename):
		cfile = open("%s.classifier" % (filename), "w")
		pickle.dump(c, cfile)
		cfile.close

	@staticmethod
	def loadClassifier(filename):
		cfile = open("%s.classifier" % (filename), "r")
		c = pickle.load(cfile)
		return c

	@staticmethod
	def getClassifiedTokens(info, text):
		if (info=="when"):
			c = Classifier.loadClassifier("classifiers/when")
			ctokens = []
			for token in Tokenizer.getNTokens(text, 5):
				fitur = FeatureExtractorWhen.getFeatureWhen(token, text)
				ctokens.append((c.classify(fitur), token))
			return ctokens
		else:
			return []

