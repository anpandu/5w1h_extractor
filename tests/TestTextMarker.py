from module.dataprovider import MDP
from module.textmarker import TextMarker

class TestTextMarker:

	@classmethod
	def setup_class(self):
		self.paragraph = MDP.get5w1h([6])[1]

	def test_getMarkedText(self):
		text = self.paragraph
		res = TextMarker.getMarkedText(text)
		assert "_bwhat_" in res
		assert "_bwho_" in res
		assert "_bwhen_" in res
		assert "_bwhere_" in res
		assert "_bwhy_" in res
		assert "_bhow_" in res

	def test_getMarkedTexts(self):
		texts = MDP.get5w1h([6])
		res = TextMarker.getMarkedTexts(texts)
		assert len(res)>1