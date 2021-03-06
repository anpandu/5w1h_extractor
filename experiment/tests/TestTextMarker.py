from module.dataprovider import MDP
from module.textmarker import TextMarker
import re
import json

class TestTextMarker:

	@classmethod
	def setup_class(self):
		self.info = MDP.get5w1h([6])[2]

	def test_getTaggedText(self):
		info = self.info
		# print json.dumps(info, default=lambda o: o.__dict__, indent=2)
		# assert 1==2
		res = TextMarker.getTaggedText(info)
		assert "[bwhat]" in res
		assert "[bwho]" in res
		assert "[bwhen]" in res
		assert "[bwhere]" in res
		assert "[bwhy]" in res
		assert "[bhow]" in res

	def test_getTaggedTexts(self):
		infos = MDP.get5w1h([6])
		res = TextMarker.getTaggedTexts(infos)
		assert len(res)>1

	def test_getOtherTaggedText(self):
		info = self.info
		res = TextMarker.getOtherTaggedText(info)
		# print res
		# print ''
		searchObj = re.findall( r'(\[b.+?\].+?\[e.+?\])', res)
		# for x in searchObj:
		# 	print x
		assert re.search(r'(\[bwhat\].+?\[ewhat\])', res)
		assert re.search(r'(\[bwho\].+?\[ewho\])', res)
		assert re.search(r'(\[bwhen\].+?\[ewhen\])', res)
		assert re.search(r'(\[bwhere\].+?\[ewhere\])', res)
		assert re.search(r'(\[bwhy\].+?\[ewhy\])', res)
		assert re.search(r'(\[bhow\].+?\[ehow\])', res)
		assert re.search(r'(\[bother\].+?\[eother\])', res)

	def test_getMarkedText(self):
		info = self.info
		mtext = TextMarker.getMarkedText(info)
		searchObj = re.findall( r'\[(.+?)\](.+?)\[.+?\]', mtext)
		# for x in searchObj:
		# 	print x
		# print mtext
		assert len(searchObj)>1

	def test_getTextLabelTuples(self):
		info = self.info
		tuples = TextMarker.getTextLabelTuples(info)
		assert len(tuples)>0
		assert tuples[0]
		assert tuples[1]

	def test_getTextLabelTuplesInSentences(self):
		info = self.info
		tuples = TextMarker.getTextLabelTuples(info)
		tupless = TextMarker.getTextLabelTuplesInSentences(info)
		# for tuples in tupless:
		# 	for tup in tuples:
		# 		print tup
		# 	print ''
		assert type(tupless) is list
		assert type(tupless[0]) is list
		assert type(tupless[0][0]) is tuple
		assert len(tuples) == len([item for tuples in tupless for item in tuples])
