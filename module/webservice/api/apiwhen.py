from module.classifier import Classifier

class ApiWhen(object):

	@staticmethod
	def getWhen(text):
	    ctokens = Classifier.getClassifiedTokens("when", text)
	    ctokenstrue = [ctoken for ctoken in ctokens if ctoken[0]==True]
	    return ctokenstrue