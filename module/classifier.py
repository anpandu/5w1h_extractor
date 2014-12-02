import nltk
import pickle
from module.tokenizer import Tokenizer
# from module.fe.fe_when import FeatureExtractorWhen
from module.featureextractor import FeatureExtractor
from module.textmarker import TextMarker

class Classifier(object):

	@staticmethod
	def train(info5w1hs):
		fiturs = []
		for info in info5w1hs:
			for tupl in TextMarker.getTextLabelTuples(info):
				# print (FeatureExtractor.getFeature(tupl[1], info.text), tupl[0])
				fiturs.append( (FeatureExtractor.getFeature(tupl[1], info.text), tupl[0]) )
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
		c = Classifier.loadClassifier("classifiers/when")
		ctokens = []
		for token in Tokenizer.getNTokens(text, 5):
			fitur = FeatureExtractor.getFeature(token, text)
			ctokens.append((c.classify(fitur), token))
		return ctokens

