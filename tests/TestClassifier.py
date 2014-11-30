import nltk
from module.classifier import Classifier
from module.dataprovider import MDP
from module.featureextractor import FeatureExtractor

class TestClassifier:

    @classmethod
    def setup_class(self):
        pass

    def test_trainWhen(self):
        temp = Classifier.trainWhen(MDP.get5w1h([6]))
        assert "classifier" in temp
        assert "fiturs" in temp