import nltk
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