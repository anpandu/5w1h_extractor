import nltk
import os
from module.classifier import Classifier
from module.dataprovider import MDP

class TestClassifier:

    @classmethod
    def setup_class(self):
        pass

    def test_train(self):
        Classifier.train(MDP.get5w1h([6]))
        temp = Classifier.train(MDP.get5w1h([6]))
        assert "classifier" in temp
        assert "fiturs" in temp

    def test_saveClassifier_loadClassifier(self):
        temp = Classifier.train(MDP.get5w1h([6]))
        c = temp["classifier"]
        Classifier.saveClassifier(c, "whentest")
        c2 = Classifier.loadClassifier("whentest")
        assert isinstance(c2, nltk.classify.naivebayes.NaiveBayesClassifier)
        os.remove("whentest.classifier")

    def test_getClassifiedTokens(self):
        text = MDP.get5w1h([6])[0].text
        ctokens = Classifier.getClassifiedTokens("when", text)
        assert len(ctokens)>1
    
    # def test_temp(self):
    #     temp = Classifier.train(MDP.get5w1h([6]))
    #     c = temp["classifier"]
    #     fiturs = temp["fiturs"]
    #     fiturst = [x for x in fiturs if (x[1]=="beg_when" or x[1]=="in_when")]
    #     fitursf = [x for x in fiturs if (x[1]!="beg_when" and x[1]!="in_when")]

    #     for x in fiturst:
    #         print x

    #     print ""
    #     print "All =\t %d" % len(fiturs)
    #     print "True features set =\t %d" % len(fiturst)
    #     print "False features set =\t %d" % len(fitursf)

    #     print "True detected as true \t\t %s" % (nltk.classify.accuracy(c, fiturst))
    #     print "False detected as False \t %s" % (nltk.classify.accuracy(c, fitursf))
    #     print "All \t\t\t\t %s" % (nltk.classify.accuracy(c, fiturs))
        
    #     assert "classifier" in temp
    #     assert "fiturs" in temp
    #     assert 1 == 2