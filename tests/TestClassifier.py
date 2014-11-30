import nltk
import os
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

    def test_saveClassifier_loadClassifier(self):
        temp = Classifier.trainWhen(MDP.get5w1h([6]))
        c = temp["classifier"]
        Classifier.saveClassifier(c, "whentest")
        c2 = Classifier.loadClassifier("whentest")
        assert isinstance(c2, nltk.classify.naivebayes.NaiveBayesClassifier)
        os.remove("whentest.classifier")