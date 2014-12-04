from module.featureextractor import FeatureExtractor
from module.textmarker import TextMarker
from module.dataprovider import MDP

class TestFeatureExtractor:

    @classmethod
    def setup_class(self):
    	# self.text1 = "Forum Indonesia untuk Transparansi Anggaran (Fitra) telah menduga PT Ghalia Indonesia Printing tak akan berhasil menyelesaikan tender naskah ujian nasional."
    	self.info = MDP.get5w1h([6])[0]
        pass

    def test_getFeature(self):
    	print FeatureExtractor.getFeature("19 Oktober 2014", "")
    	assert 1==1

    def test_getFeaturesInSentence(self):
    	lts = TextMarker.getTextLabelTuplesInSentences(self.info)[0]
    	featuress = FeatureExtractor.getFeaturesInSentence(lts)
    	for x in featuress:
    		print x
    	assert 1==2

	def test_runCommand(self):
		command = "echo hahaha"
		results = FeatureExtractor.runCommand(command)
		assert results[0]=="hahaha\n"