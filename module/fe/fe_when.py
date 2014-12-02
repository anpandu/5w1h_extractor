from base_fe import BaseFeatureExtractor
import re

class FeatureExtractorWhen(object):

	@staticmethod
	def getFeature(word, doc):
		features = {}
		# features["_word"] = word
		# pts = FeatureExtractor.prevTokenInSentences(word, doc)
		# nts = FeatureExtractor.nextTokenInSentences(word, doc)
		# features["prev"] = pts[0] if len(pts)>0 else ""
		# features["next"] = nts[0] if len(nts)>0 else ""
		features["daynames"] = FeatureExtractorWhen.isContainingDayNames(word)
		features["monthnames"] = FeatureExtractorWhen.isContainingMonthNames(word)
		features["datenumbers"] = FeatureExtractorWhen.isContainingDateNumbers(word)
		features["year"] = FeatureExtractorWhen.isContainingYear(word)
		features["slash"] = BaseFeatureExtractor.isContainingString("/",word)
		features["ntoken"] = BaseFeatureExtractor.countToken(word)
		return features

	@staticmethod
	def isContainingDayNames(word):
		daynames = ["Ahad", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
		res = False
		for dayname in daynames:
			res = res or BaseFeatureExtractor.isContainingString(dayname, word)
		return res

	@staticmethod
	def isContainingMonthNames(word):
		monthnames = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "November", "Desember"]
		res = False
		for monthname in monthnames:
			res = res or BaseFeatureExtractor.isContainingString(monthname, word)
		return res

	@staticmethod
	def isContainingDateNumbers(word):
		res = False
		for dn in range(1,31):
			dn_str = "%d" % (dn)
			res = res or BaseFeatureExtractor.isContainingString(dn_str, word)
		return res

	@staticmethod
	def isContainingYear(word):
		find = re.findall(r'20\d\d', word)
		res = len(find)>0
		return res