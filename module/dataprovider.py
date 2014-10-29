import MySQLdb


class MDP(object):

	def __init__(self):
		self.conn = MySQLdb.connect(host="localhost", 
		                     user="tugasakhir", 
		                     passwd="belumselesai", 
		                     db="tugasakhir")
		self.cur = self.conn.cursor()

	def printArray(self, arr):
		for x in arr:
			print x

	def getQuery(self, _sql):
		try:
			self.cur.execute(_sql)
			result = []
			for res in self.cur.fetchall():
				result.append(res)
			return result
			self.conn.commit()
		except:
			return []
			self.conn.rollback()

	def get5w1h(self, limit=0):
		if (limit==0):
			return self.getQuery("SELECT 5w1hs.what, 5w1hs.who, 5w1hs.when, 5w1hs.where, 5w1hs.why, 5w1hs.how, articles.text, articles.title FROM 5w1hs, articles WHERE 5w1hs.article_id = articles.id AND user_id=6")



class TextDP(object):

	def __init__(self):
		pass

	# def getIndoWordList(self):
	# 	arr = open("indowordlists/05-ivanlanin2011-sort-alpha.lst").read().split("\n")
	# 	return arr[:len(arr)-1]

	# def getPropDescCWWordList(self):
	# 	arr = open("indowordlists/propdesc_cw.lst").read().split("\n")
	# 	return arr[:len(arr)-1]


