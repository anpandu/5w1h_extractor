import json
from sys import argv

arg = ""
if len(argv)>1:
	arg = argv[1]

from module.classifier import Classifier
from module.dataprovider import MDP
from module.featureextractor import FeatureExtractor
from module.tokenizer import Tokenizer
import nltk

infos = MDP.get5w1h([6])
results = []

for x in infos:
	when = x.when
	twhen = Tokenizer.getTokens(x.when)
	prevwhen = FeatureExtractor.prevToken(x.when, x.text)
	nextwhen = FeatureExtractor.nextToken(x.when, x.text)
	res = {'twhen':twhen, 'prevwhen':prevwhen, 'nextwhen':nextwhen}
	results.append(res)

if (arg=="json"):
	## JSON
	print json.dumps(results, indent=2)
elif(arg=="log"):
	## LOG
	print "=== twhen ==="
	for x in results:
		print x["twhen"]
	print ""
	print "=== prevwhen ==="
	for x in results:
		print x["prevwhen"]
	print ""
	print "=== nextwhen ==="
	for x in results:
		print x["nextwhen"]
	print ""
else:
	pass