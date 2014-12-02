from module.dataprovider import MDP
from module.textmarker import TextMarker
import re
import json

class TestTextMarker:

	@classmethod
	def setup_class(self):
		self.info = MDP.get5w1h([6])[1]

	def test_getMarkedText(self):
		info = self.info
		# print json.dumps(info, default=lambda o: o.__dict__, indent=2)
		# assert 1==2
		res = TextMarker.getMarkedText(info)
		assert "[bwhat]" in res
		assert "[bwho]" in res
		assert "[bwhen]" in res
		assert "[bwhere]" in res
		assert "[bwhy]" in res
		assert "[bhow]" in res

	def test_getMarkedTexts(self):
		infos = MDP.get5w1h([6])
		res = TextMarker.getMarkedTexts(infos)
		assert len(res)>1

	def test_getOtherMarkedText(self):
		info = self.info
		res = TextMarker.getMarkedText(info)
		res2 = TextMarker.getOtherMarkedText(res)
		print res
		print ''
		searchObj = re.findall( r'(\[b.+?\].+?\[e.+?\])', res2)
		for x in searchObj:
			print x
		assert re.search(r'(\[bwhat\].+?\[ewhat\])', res2)
		assert re.search(r'(\[bwho\].+?\[ewho\])', res2)
		assert re.search(r'(\[bwhen\].+?\[ewhen\])', res2)
		assert re.search(r'(\[bwhere\].+?\[ewhere\])', res2)
		assert re.search(r'(\[bwhy\].+?\[ewhy\])', res2)
		assert re.search(r'(\[bhow\].+?\[ehow\])', res2)
		assert re.search(r'(\[bother\].+?\[eother\])', res2)