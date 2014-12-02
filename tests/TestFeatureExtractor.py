from module.featureextractor import FeatureExtractor

class TestFeatureExtractor:

    @classmethod
    def setup_class(self):
        pass

    def test_getFeature(self):
    	print FeatureExtractor.getFeature("19 Oktober 2014", "")
    	assert 1==1