from module.featureextractor import FeatureExtractor
from module.textmarker import TextMarker
from module.dataprovider import MDP

class TestFeatureExtractor:

    @classmethod
    def setup_class(self):
    	self.info = MDP.get5w1h([6])[1]
        self.infos =  MDP.get5w1h([6])
        self.infos2 = []
        for x in [2]:
            self.infos2.append(self.infos[x-1])
        self.infos = self.infos2

    def test_getFeature(self):
    	print FeatureExtractor.getFeature("19 Oktober 2014", "")
    	assert 1==1

    def test_getFitursCSV(self):
        csvstr = FeatureExtractor.getFitursCSV(self.infos)
        # print csvstr
        assert 1==1

    def test_getFeaturesInSentence(self):
    	lts = TextMarker.getTextLabelTuplesInSentences(self.info)
    	fword = FeatureExtractor.getFeaturesInSentence(lts[0])[0][0]
    	# for lt in lts:
    	# 	featuress = FeatureExtractor.getFeaturesInSentence(lt)
    	# 	print ''
    	# 	for x in featuress:
    	# 		print x
        assert "tok" in fword
        assert "tokkind" in fword
        assert "ne" in fword
        assert "contextfe" in fword
        assert "morphfe" in fword
        assert "posfe" in fword
        assert "bef1tok" in fword
        assert "bef1tokkind" in fword
        assert "bef1ne" in fword
        assert "bef1contextfe" in fword
        assert "bef1morphfe" in fword
        assert "bef1posfe" in fword
        assert "bef2tok" in fword
        assert "bef2tokkind" in fword
        assert "bef2ne" in fword
        assert "bef2contextfe" in fword
        assert "bef2morphfe" in fword
        assert "bef2posfe" in fword
        # assert 1==2

    def test_runCommand(self):
    	command = "echo hahaha"
    	results = FeatureExtractor.runCommand(command)
    	assert results[0]=="hahaha\n"