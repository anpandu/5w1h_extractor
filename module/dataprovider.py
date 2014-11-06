import MySQLdb
from Info5W1H import Info5W1H


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

	def get5w1h(self, ids=[]):
		ids = [str(i) for i in ids]
		res = []
		for uid in ids:
			res += self._get5w1h(uid)
		return res

	def _get5w1h(self, uid):
		que_res = self.getQuery("SELECT 5w1hs.what, 5w1hs.who, 5w1hs.when, 5w1hs.where, 5w1hs.why, 5w1hs.how, articles.text, articles.title FROM 5w1hs, articles WHERE 5w1hs.article_id = articles.id AND user_id=%s" % (uid))
		res = [Info5W1H(item[0], item[1], item[2], item[3], item[4], item[5], item[6]) for item in que_res]
		return res


