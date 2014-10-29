from dataprovider import MDP

class TextMarker(object):

	def __init__(self):
		self.mdp = MDP()
		self.items = self.mdp.get5w1h()
		self.text_marked = []
		self.bmarks = ['_bwhat_', '_bwho_', '_bwhen_', '_bwhere_', '_bwhy_', '_bhow_']
		self.emarks = ['_ewhat_', '_ewho_', '_ewhen_', '_ewhere_', '_ewhy_', '_ehow_']

	def getMarkedTexts(self):
		for item in self.items:
			text = item[6]
			for i in xrange(0,5):		
				if (item[i]!='-' and item[i]!=''):
					begin = text.find(item[i])
					if (begin>-1):
						text = text[:begin] + self.bmarks[i] + text[begin:]
						begin = text.find(item[i])
						end = begin+len(item[i])
						text = text[:end] + self.emarks[i] + text[end:]
			self.text_marked.append(text)
		return self.text_marked