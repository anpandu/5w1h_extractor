import sys
sys.path.insert(0,"../module")

from dataprovider import MDP
from tokenizer import Tokenizer
from featureextractor import FeatureExtractor

tokenizer = Tokenizer()
mdp = MDP()
fe = FeatureExtractor()


user_ids = [6]
info5w1hs = mdp.get5w1h(user_ids)


texts = [item.text for item in info5w1hs]
text = texts[0]

for x in info5w1hs[0].sentences:
	print x

for x in info5w1hs:
	print x.where