from module.fe.base_fe import BaseFeatureExtractor

class TestBaseFeatureExtractor:

    @classmethod
    def setup_class(self):
        self.paragraph1 = "Mama, just killed a man, Put a gun against his head, Pulled my trigger, now he's dead. Mama, life had just begun, but now I've gone and thrown it all away."

    def test_freq(self):
        assert BaseFeatureExtractor.freq("Mama", self.paragraph1) == 2

    def test_prevToken(self):
        assert BaseFeatureExtractor.prevToken("Mama", self.paragraph1) == ['_begin_', '.']
        assert BaseFeatureExtractor.prevToken("trigger", self.paragraph1) == ['my']
        assert BaseFeatureExtractor.prevToken("poop", self.paragraph1) == []
        assert BaseFeatureExtractor.prevToken("", self.paragraph1) == []
        assert BaseFeatureExtractor.prevToken("Mama, just", self.paragraph1) == ['_begin_']

    def test_nextToken(self):
        assert BaseFeatureExtractor.nextToken(".", self.paragraph1) == ['Mama', '_end_']
        assert BaseFeatureExtractor.nextToken("against", self.paragraph1) == ['his']
        assert BaseFeatureExtractor.nextToken("poop", self.paragraph1) == []
        assert BaseFeatureExtractor.nextToken("", self.paragraph1) == []
        assert BaseFeatureExtractor.nextToken("all away.", self.paragraph1) == ['_end_']

    def test_prevTokenInSentences(self):
        assert BaseFeatureExtractor.prevTokenInSentences("Mama", self.paragraph1) == ['_begin_', '_begin_']
        assert BaseFeatureExtractor.prevTokenInSentences("Mama, just", self.paragraph1) == ['_begin_']

    def test_nextTokenInSentences(self):
        assert BaseFeatureExtractor.nextTokenInSentences("all away", self.paragraph1) == ['_end_']
        assert BaseFeatureExtractor.nextTokenInSentences("he's dead", self.paragraph1) == ['_end_']
        assert BaseFeatureExtractor.nextTokenInSentences("dead", self.paragraph1) == ['_end_']

    def test_isIncludingString(self):
        assert BaseFeatureExtractor.isContainingString("ll", "hello") == True
        assert BaseFeatureExtractor.isContainingString("/", "Sabtu, 11/9") == True
        assert BaseFeatureExtractor.isContainingString("Sabtu", "Sabtu (11/9)") == True
        assert BaseFeatureExtractor.isContainingString("sabtu", "Sabtu (11/9)") == False

    def test_countToken(self):
        assert BaseFeatureExtractor.countToken("hello") == 1
        assert BaseFeatureExtractor.countToken("") == 0
        assert BaseFeatureExtractor.countToken("Sabtu (11/9)") == 4