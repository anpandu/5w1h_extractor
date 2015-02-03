from module.dataprovider import MDP
from random import randrange

class ApiNews(object):

	@staticmethod
	def getRandomNews():
		texts = [item.text for item in MDP.get5w1h([6])]
		text = texts[randrange(len(texts))]
		return text