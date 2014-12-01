import nltk
import os
from module.classifier import Classifier
from module.dataprovider import MDP
from module.featureextractor import FeatureExtractor
from module.fe.fe_when import FeatureExtractorWhen

class TestClassifier:

    @classmethod
    def setup_class(self):
        pass

    @classmethod
    def teardown_class(self):
        os.remove("whentest.classifier")

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

    def test_classify(self):
        c = Classifier.loadClassifier("whentest")
        fitur = FeatureExtractorWhen.getFeatureWhen("Minggu, 19 Agustus 2013", "")
        assert Classifier.classify(c, fitur)