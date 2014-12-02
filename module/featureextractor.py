from tokenizer import Tokenizer
from fe.fe_when import FeatureExtractorWhen

class FeatureExtractor(object):

	@staticmethod
	def getFeature(word, text):
		fwhen = FeatureExtractorWhen.getFeature(word, "")
		return fwhen