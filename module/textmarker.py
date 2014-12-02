from dataprovider import MDP
from tokenizer import Tokenizer

class TextMarker(object):

	btags = ['[bwhat]', '[bwho]', '[bwhen]', '[bwhere]', '[bwhy]', '[bhow]']
	etags = ['[ewhat]', '[ewho]', '[ewhen]', '[ewhere]', '[ewhy]', '[ehow]']
	othertags = ['[bother]', '[eother]']

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
					text = text[:begin] + TextMarker.btags[i] + text[begin:]
					begin = text.find(getattr(info, propname))
					end = begin+len(getattr(info, propname))
					text = text[:end] + TextMarker.etags[i] + text[end:]
		return text

	@staticmethod
	def getOtherMarkedText(markedtext):
		btags2 = ['B_WHAT', 'B_WHO', 'B_WHEN', 'B_WHERE', 'B_WHY', 'B_HOW']
		etags2 = ['E_WHAT', 'E_WHO', 'E_WHEN', 'E_WHERE', 'E_WHY', 'E_HOW']

		for i, tag in enumerate(btags2):
			markedtext = markedtext.replace(TextMarker.btags[i], tag)
		for i, tag in enumerate(etags2):
			markedtext = markedtext.replace(TextMarker.etags[i], tag)	

		text = ""
		state = 0
		for token in Tokenizer.getTokens(markedtext):
			if (reduce( (lambda x, y: x or y), list(map((lambda x: x in token), btags2)) )):
				state += 1
			if (state==0):
				# print "%s\t%s" % (state, TextMarker.othertags[0] + token + TextMarker.othertags[1])
				text += TextMarker.othertags[0] + token + TextMarker.othertags[1]
			else:
				# print "%s\t%s" % (state, token)
				text += token + " "
			if (reduce( (lambda x, y: x or y), list(map((lambda x: x in token), etags2)) )):
				state -= 1

		for i, tag in enumerate(TextMarker.btags):
			text = text.replace(btags2[i], tag)
		for i, tag in enumerate(TextMarker.etags):
			text = text.replace(etags2[i], tag)	

		return text