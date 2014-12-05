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
		# print sentence
		finanlp = FeatureExtractor.runCommand("java -jar module/inanlp/adapter_inanlp.jar '%s'" % sentence)
		finanlp = [r[:-1] for r in finanlp] # remove \n 
		for idx, tup in enumerate(tuples):
			regexres = re.findall( r'\[(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\]', finanlp[idx])[0]
			# features = FeatureExtractorWhen.getFeature(tup[1], "")
			features = {}
			features["tok"] = regexres[0]
			features["tokkind"] = regexres[1]
			features["ne"] = regexres[2]
			features["contextfe"] = regexres[3]
			features["morphfe"] = regexres[4]
			features["posfe"] = regexres[5]
			label = tup[0]
			featuress.append((features, label))
			# print features
		# print ''
		bef1featuress = []
		for i in range(0,len(featuress)):
			if (i-1>=0):
				bef1featuress.append(featuress[i-1])
			else:
				bef1featuress.append(({'morphfe': '', 'posfe': '', 'ne': 'BEGIN', 'tok': '', 'contextfe': '', 'tokkind': 'BEGIN'}, 'BEGIN'))
		for i in range(0,len(featuress)):
			featuress[i][0]["bef1tok"] = bef1featuress[i][0]["tok"]
			featuress[i][0]["bef1tokkind"] = bef1featuress[i][0]["tokkind"]
			featuress[i][0]["bef1ne"] = bef1featuress[i][0]["ne"]
			featuress[i][0]["bef1contextfe"] = bef1featuress[i][0]["contextfe"]
			featuress[i][0]["bef1morphfe"] = bef1featuress[i][0]["morphfe"]
			featuress[i][0]["bef1posfe"] = bef1featuress[i][0]["posfe"]
			featuress[i][0]["bef1class"] = bef1featuress[i][1]
		bef2featuress = []
		for i in range(0,len(featuress)):
			if (i-2>=0):
				bef2featuress.append(featuress[i-2])
			else:
				bef2featuress.append(({'morphfe': '', 'posfe': '', 'ne': 'BEGIN', 'tok': '', 'contextfe': '', 'tokkind': 'BEGIN'}, 'BEGIN'))
		for i in range(0,len(featuress)):
			featuress[i][0]["bef2tok"] = bef2featuress[i][0]["tok"]
			featuress[i][0]["bef2tokkind"] = bef2featuress[i][0]["tokkind"]
			featuress[i][0]["bef2ne"] = bef2featuress[i][0]["ne"]
			featuress[i][0]["bef2contextfe"] = bef2featuress[i][0]["contextfe"]
			featuress[i][0]["bef2morphfe"] = bef2featuress[i][0]["morphfe"]
			featuress[i][0]["bef2posfe"] = bef2featuress[i][0]["posfe"]
			featuress[i][0]["bef2class"] = bef2featuress[i][1]
		# for x in featuress:
		# 	print x
		return featuress

	@staticmethod
	def runCommand(command):
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return p.stdout.readlines()