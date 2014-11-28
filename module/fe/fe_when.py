from ..featureextractor import FeatureExtractor

class FeatureExtractorWhen(object):

	@staticmethod
	def getFeatureWhen(word, doc):
		pts = FeatureExtractor.prevTokenInSentences(word, doc)
		nts = FeatureExtractor.nextTokenInSentences(word, doc)
		features = {}
		# features["_word"] = word
		features["prev"] = pts[0] if len(pts)>0 else ""
		features["next"] = nts[0] if len(nts)>0 else ""
		# features["freq"] = FeatureExtractor.freq(word, doc)
		return features

	@staticmethod
	def isContainingDayNames(word):
		daynames = ["Ahad", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
		res = False
		for dayname in daynames:
			res = res or FeatureExtractor.isIncludingString(dayname, word)
		return res

	@staticmethod
	def isContainingMonthNames(word):
		monthnames = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "November", "Desember"]
		res = False
		for monthname in monthnames:
			res = res or FeatureExtractor.isIncludingString(monthname, word)
		return res

	@staticmethod
	def isContainingDateNumbers(word):
		res = False
		for dn in range(1,31):
			dn_str = "%d" % (dn)
			res = res or FeatureExtractor.isIncludingString(dn_str, word)
		return res