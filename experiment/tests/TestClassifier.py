import nltk
import os
from module.classifier import Classifier
from module.dataprovider import MDP

class TestClassifier:

    @classmethod
    def setup_class(self):
        self.infos =  MDP.get5w1h([6])
        self.infos2 = []
        for x in [2]:
            self.infos2.append(self.infos[x-1])
        self.infos = self.infos2

    def test_train(self):
        temp = Classifier.train(self.infos)
        assert "classifier" in temp
        assert "fiturs" in temp

    def test_saveClassifier_loadClassifier(self):
        temp = Classifier.train(self.infos)
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
    #     infos = MDP.get5w1h([6])
    #     infos2 = []
    #     for x in [2,4,6,7,9,10,13,16,17,18,23,24,27]:
    #         infos2.append(infos[x-1])
    #     infos = infos2
    #     temp = Classifier.train(infos)
    #     c = temp["classifier"]
    #     fiturs = temp["fiturs"]

    #     fiturs0 = [x for x in fiturs if (x[1]=="other")]
    #     fiturs1 = [x for x in fiturs if (x[1]=="beg_what")]
    #     fiturs2 = [x for x in fiturs if (x[1]=="beg_who")]
    #     fiturs3 = [x for x in fiturs if (x[1]=="beg_when")]
    #     fiturs4 = [x for x in fiturs if (x[1]=="beg_where")]
    #     fiturs5 = [x for x in fiturs if (x[1]=="beg_why")]
    #     fiturs6 = [x for x in fiturs if (x[1]=="beg_how")]
    #     fiturs1b = [x for x in fiturs if (x[1]=="in_what")]
    #     fiturs2b = [x for x in fiturs if (x[1]=="in_who")]
    #     fiturs3b = [x for x in fiturs if (x[1]=="in_when")]
    #     fiturs4b = [x for x in fiturs if (x[1]=="in_where")]
    #     fiturs5b = [x for x in fiturs if (x[1]=="in_why")]
    #     fiturs6b = [x for x in fiturs if (x[1]=="in_how")]

    #     # for x in fiturst:
    #     #     print x

    #     print ""
    #     print "All =\t %d" % len(fiturs)
    #     # print "True features set =\t %d" % len(fiturst)
    #     # print "False features set =\t %d" % len(fitursf)
    #     # print "True detected as true \t\t %s" % (nltk.classify.accuracy(c, fiturst))
    #     # print "False detected as False \t %s" % (nltk.classify.accuracy(c, fitursf))

    #     print ''
    #     print "beg_what detected as beg_what \t %s" % (nltk.classify.accuracy(c, fiturs1))
    #     print "beg_who detected as beg_who \t %s" % (nltk.classify.accuracy(c, fiturs2))
    #     print "beg_when detected as beg_when \t %s" % (nltk.classify.accuracy(c, fiturs3))
    #     print "beg_where detected as beg_wh.. \t %s" % (nltk.classify.accuracy(c, fiturs4))
    #     print "beg_why detected as beg_why \t %s" % (nltk.classify.accuracy(c, fiturs5))
    #     print "beg_how detected as beg_how \t %s" % (nltk.classify.accuracy(c, fiturs6))
    #     print ''
        
    #     print "in_what detected as in_what \t %s" % (nltk.classify.accuracy(c, fiturs1b))
    #     print "in_who detected as in_who \t %s" % (nltk.classify.accuracy(c, fiturs2b))
    #     print "in_when detected as in_when \t %s" % (nltk.classify.accuracy(c, fiturs3b))
    #     print "in_where detected as in_where \t %s" % (nltk.classify.accuracy(c, fiturs4b))
    #     print "in_why detected as in_why \t %s" % (nltk.classify.accuracy(c, fiturs5b))
    #     print "in_how detected as in_how \t %s" % (nltk.classify.accuracy(c, fiturs6b))
    #     print ''
    #     print "other detected as other \t %s" % (nltk.classify.accuracy(c, fiturs0))
    #     print ''

    #     print "All \t\t\t\t %s" % (nltk.classify.accuracy(c, fiturs))
        
    #     assert "classifier" in temp
    #     assert "fiturs" in temp
    #     assert 1 == 2