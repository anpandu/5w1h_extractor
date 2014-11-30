import json
from sys import argv

arg = ""
if len(argv)>1:
	arg = argv[1]

from module.classifier import Classifier
from module.dataprovider import MDP
from module.featureextractor import FeatureExtractor
from module.fe.fe_when import FeatureExtractorWhen
from module.tokenizer import Tokenizer
import nltk

infos = MDP.get5w1h([6])
results = []

for x in infos:
	when = x.when
	twhen = Tokenizer.getTokens(x.when)
	prevwhen = FeatureExtractor.prevToken(x.when, x.text)
	nextwhen = FeatureExtractor.nextToken(x.when, x.text)
	ntoken = FeatureExtractor.countToken(when)
	day = FeatureExtractorWhen.isContainingDayNames(when)
	date = FeatureExtractorWhen.isContainingDateNumbers(when)
	month = FeatureExtractorWhen.isContainingMonthNames(when)
	year = FeatureExtractorWhen.isContainingYear(when)
	slash = FeatureExtractor.isIncludingString("/",when)
	res = {'twhen':twhen, 'prevwhen':prevwhen, 'nextwhen':nextwhen, 'ntoken':ntoken, 'day':day, 'date':date, 'month':month, 'year':year, 'slash':slash}
	results.append(res)

if (arg=="json"):
	## JSON
	print json.dumps(results, indent=2)
elif(arg=="log"):
	## LOG
	print "=== token ==="
	for x in results:
		print x["twhen"]
	print ""
	
	print "=== jumlah token ==="
	for x in results:
		print x["ntoken"]
	print ""
	
	print "=== mengandung nama hari ==="
	for x in results:
		print x["day"]
	print ""
	
	print "=== mengandung angka 1-31 (tanggal) ==="
	for x in results:
		print x["date"]
	print ""
	
	print "=== mengandung nama bulan ==="
	for x in results:
		print x["month"]
	print ""
	
	print "=== mengandung nama tahun ==="
	for x in results:
		print x["year"]
	print ""

	print "=== mengandung '/' ==="
	for x in results:
		print x["slash"]
	print ""

	print "=== prev token ==="
	for x in results:
		print x["prevwhen"]
	print ""

	print "=== next token ==="
	for x in results:
		print x["nextwhen"]
	print ""
else:
	pass