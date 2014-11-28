from module.featureextractor import FeatureExtractor

class TestFeatureExtractor:

    @classmethod
    def setup_class(self):
        self.paragraph1 = "Mama, just killed a man, Put a gun against his head, Pulled my trigger, now he's dead. Mama, life had just begun, but now I've gone and thrown it all away."

    def test_freq(self):
        assert FeatureExtractor.freq("Mama", self.paragraph1) == 2

    def test_prevToken(self):
        assert FeatureExtractor.prevToken("Mama", self.paragraph1) == ['_begin_', '.']
        assert FeatureExtractor.prevToken("trigger", self.paragraph1) == ['my']
        assert FeatureExtractor.prevToken("poop", self.paragraph1) == []
        assert FeatureExtractor.prevToken("", self.paragraph1) == []
        assert FeatureExtractor.prevToken("Mama, just", self.paragraph1) == ['_begin_']

    def test_nextToken(self):
        assert FeatureExtractor.nextToken(".", self.paragraph1) == ['Mama', '_end_']
        assert FeatureExtractor.nextToken("against", self.paragraph1) == ['his']
        assert FeatureExtractor.nextToken("poop", self.paragraph1) == []
        assert FeatureExtractor.nextToken("", self.paragraph1) == []
        assert FeatureExtractor.nextToken("all away.", self.paragraph1) == ['_end_']

    def test_prevTokenInSentences(self):
        assert FeatureExtractor.prevTokenInSentences("Mama", self.paragraph1) == ['_begin_', '_begin_']
        assert FeatureExtractor.prevTokenInSentences("Mama, just", self.paragraph1) == ['_begin_']

    def test_nextTokenInSentences(self):
        assert FeatureExtractor.nextTokenInSentences("all away", self.paragraph1) == ['_end_']
        assert FeatureExtractor.nextTokenInSentences("he's dead", self.paragraph1) == ['_end_']
        assert FeatureExtractor.nextTokenInSentences("dead", self.paragraph1) == ['_end_']

    def test_isIncludingString(self):
        assert FeatureExtractor.isIncludingString("ll", "hello") == True
        assert FeatureExtractor.isIncludingString("/", "Sabtu, 11/9") == True
        assert FeatureExtractor.isIncludingString("Sabtu", "Sabtu (11/9)") == True
        assert FeatureExtractor.isIncludingString("Sabtu ", "Sabtu (11/9)") == False
        assert FeatureExtractor.isIncludingString("sabtu", "Sabtu (11/9)") == False