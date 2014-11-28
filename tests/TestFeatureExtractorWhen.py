from module.fe.fe_when import FeatureExtractorWhen

class TestFeatureExtractorWhen:

    @classmethod
    def setup_class(self):
        pass

    def test_isContainingDayNames(self):
        assert FeatureExtractorWhen.isContainingDayNames("Sabtu, (11/9)") == True
        assert FeatureExtractorWhen.isContainingDayNames("Ahad, 14 April 2013") == True
        assert FeatureExtractorWhen.isContainingDayNames("Kamis, 18 April 2013") == True
        assert FeatureExtractorWhen.isContainingDayNames("Ahad (14/4)") == True
        assert FeatureExtractorWhen.isContainingDayNames("15 April 2013") == False