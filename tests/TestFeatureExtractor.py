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

    def test_nextToken(self):
        assert FeatureExtractor.nextToken(".", self.paragraph1) == ['Mama', '_end_']
        assert FeatureExtractor.nextToken("against", self.paragraph1) == ['his']
        assert FeatureExtractor.nextToken("poop", self.paragraph1) == []