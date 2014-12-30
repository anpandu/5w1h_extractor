from module.predictor import Predictor
from module.dataprovider import MDP
import subprocess

class TestPredictor:

    @classmethod
    def setup_class(self):
		self.info = MDP.get5w1h([6])[1]		
		self.infos =  MDP.get5w1h([6])
		self.infos2 = []
		for x in [2]:
			self.infos2.append(self.infos[x-1])
		self.infos = self.infos2	

    def test_tes(self):
    	res = Predictor.getPrediction(self.infos)
    	for i, x in enumerate(res):
    		print i, x
    	print len(res)
    	assert 1 == 2