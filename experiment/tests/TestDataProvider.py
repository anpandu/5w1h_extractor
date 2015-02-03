from module.dataprovider import MDP

class TestDataProvider:

    def test_isConnect(self):
    	res = MDP.isConnect()
    	assert res!=""

    def test__getQueryText(self):
    	text = MDP._getQueryText(6)
    	assert text == "SELECT 5w1hs.what, 5w1hs.who, 5w1hs.when, 5w1hs.where, 5w1hs.why, 5w1hs.how, articles.text, articles.title FROM 5w1hs, articles WHERE 5w1hs.article_id = articles.id AND user_id=6"

    def test_get5w1h(self):
    	texts = [item.text for item in MDP.get5w1h([6])]
    	assert len(texts) == 30

