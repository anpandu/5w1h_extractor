from tokenizer import Tokenizer
from fe.fe_when import FeatureExtractorWhen
import subprocess

class FeatureExtractor(object):

	@staticmethod
	def getFeature(word, text):
		fwhen = FeatureExtractorWhen.getFeature(word, "")
		return fwhen

	@staticmethod
	def runCommand(command):
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return p.stdout.readlines()