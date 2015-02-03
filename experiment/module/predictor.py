from module.featureextractor import FeatureExtractor
from module.dataprovider import MDP
from module.tokenizer import Tokenizer
import subprocess
import re

class Predictor(object):

	@staticmethod
	def runCommand(command):
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return p.stdout.readlines()

	@staticmethod
	def getPredictionTuple(infos):
		csvstr = FeatureExtractor.getFitursCSV(infos)

		pred_file = open("predictortemp.csv", "wb")
		pred_file.write(csvstr);
		pred_file.close()

		Predictor.runCommand("java -cp module/weka/weka.jar weka.core.converters.CSVLoader predictortemp.csv > predictortemp.arff")

		pred_file = open("predictortemp.arff", "r+")
		pred_arff = pred_file.read();
		pred_file.close()

		temp_file = open("module/weka/template.arff", "r+")
		temp_arff = temp_file.read();
		temp_file.close()
		
		header_template = re.findall(r'^([\x00-\x7F]*)@data', temp_arff)[0]
		data = re.findall(r'(@data[\x00-\x7F]*)$', pred_arff)[0]

		pred_file = open("predictortemp_fix.arff", "wb")
		pred_file.write("%s%s" % (header_template, data));
		pred_file.close()

		pred_output = Predictor.runCommand("java -cp module/weka/weka.jar weka.classifiers.bayes.NaiveBayes -T predictortemp_fix.arff -l module/weka/nb.model -p 0")
		pred_output = [r[:-1] for r in pred_output] # remove \n 
		Predictor.runCommand("rm predictortemp*")

		pred_output_text = "\n".join(pred_output[5:])

		regexres = re.findall(r'\s+(.*?)\s+(.*?):(.*?)\s+(.*?):(.*?)\s\s\s(.+?)\s\s\s(.*?)\s*\n', pred_output_text)
		regexrescl = []
		for i, item in enumerate(regexres):
			item_append = (int(item[0]), int(item[1]), item[2], int(item[3]), item[4], item[5], float(item[6]) )
			regexrescl += [item_append]

		res = []
		tokens = Tokenizer.getTokens(infos[0].text)
		for i, item in enumerate(regexrescl):
			res += [(item[3], item[4], item[6], tokens[i])]
		return res

	@staticmethod
	def getPrediction(infos):
		res = Predictor.getPredictionTuple(infos)
		return res
