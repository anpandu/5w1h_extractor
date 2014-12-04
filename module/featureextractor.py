from tokenizer import Tokenizer
from fe.fe_when import FeatureExtractorWhen
import subprocess
import re

class FeatureExtractor(object):

	@staticmethod
	def getFeature(word, text):
		fwhen = FeatureExtractorWhen.getFeature(word, "")
		return fwhen

	@staticmethod
	def getFeaturesInSentence(tuples):
		featuress = []
		# print tuples
		sentence = ' '.join([tupl[1] for tupl in tuples])
		finanlp = FeatureExtractor.runCommand("java -jar module/inanlp/adapter_inanlp.jar '%s'" % sentence)
		finanlp = [r[:-1] for r in finanlp] # remove \n 
		for idx, tup in enumerate(tuples):
			regexres = re.findall( r'\[(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\]', finanlp[idx])[0]
			# features = FeatureExtractorWhen.getFeature(tup[1], "")
			features = {}
			features["Token"] = regexres[0]
			features["TokenKind"] = regexres[1]
			features["NE"] = regexres[2]
			features["ContextualFeature"] = regexres[3]
			features["MorphologicalFeature"] = regexres[4]
			features["POSFeature"] = regexres[5]
			label = tup[0]
			featuress.append((features, label))
			# print tup
		print ''
		return featuress

	@staticmethod
	def runCommand(command):
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return p.stdout.readlines()