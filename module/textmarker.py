from dataprovider import MDP

class TextMarker(object):

	bmarks = ['_bwhat_', '_bwho_', '_bwhen_', '_bwhere_', '_bwhy_', '_bhow_']
	emarks = ['_ewhat_', '_ewho_', '_ewhen_', '_ewhere_', '_ewhy_', '_ehow_']

	@staticmethod
	def getMarkedTexts(infos):
		text_marked = [TextMarker.getMarkedText(info) for info in infos]
		return text_marked

	@staticmethod
	def getMarkedText(info):
		text = getattr(info, "text")
		for i, propname in enumerate(["what", "who", "when", "where", "why", "how"]):
			if (getattr(info, propname)!='-' and getattr(info, propname)!=''):
				begin = text.find(getattr(info, propname))
				if (begin>-1):
					text = text[:begin] + TextMarker.bmarks[i] + text[begin:]
					begin = text.find(getattr(info, propname))
					end = begin+len(getattr(info, propname))
					text = text[:end] + TextMarker.emarks[i] + text[end:]
		return text