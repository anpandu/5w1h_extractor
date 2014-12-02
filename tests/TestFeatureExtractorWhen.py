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

    def test_isContainingMonthNames(self):
        assert FeatureExtractorWhen.isContainingMonthNames("Ahad, 14 April 2013") == True
        assert FeatureExtractorWhen.isContainingMonthNames("Kamis, 18 Januari") == True
        assert FeatureExtractorWhen.isContainingMonthNames("15 April 2013") == True
        assert FeatureExtractorWhen.isContainingMonthNames("15 april 2013") == False
        assert FeatureExtractorWhen.isContainingMonthNames("Ahad (14/4)") == False
        assert FeatureExtractorWhen.isContainingMonthNames("Sabtu, (11/9)") == False

    def test_isContainingDateNumbers(self):
        assert FeatureExtractorWhen.isContainingDateNumbers("Ahad, 31 Mei") == True
        assert FeatureExtractorWhen.isContainingDateNumbers("1 April 2013") == True
        assert FeatureExtractorWhen.isContainingDateNumbers("Ahad (31/5)") == True
        assert FeatureExtractorWhen.isContainingDateNumbers("Sabtu") == False

    def test_isContainingYear(self):
        assert FeatureExtractorWhen.isContainingYear("2014") == True
        assert FeatureExtractorWhen.isContainingYear("201a") == False
        assert FeatureExtractorWhen.isContainingYear("2114") == False
        assert FeatureExtractorWhen.isContainingYear("1 April 2013") == True

    def test_getFeatureWhen(self):
        res = FeatureExtractorWhen.getFeatureWhen("Ahad, 14 April 2013", "")
        assert "ntoken" in res
        assert "daynames" in res
        assert "datenumbers" in res
        assert "monthnames" in res
        assert "year" in res
        assert "slash" in res