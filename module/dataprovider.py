import MySQLdb
from Info5W1H import Info5W1H


class MDP(object):

	conn = MySQLdb.connect(host="localhost", 
	                     user="tugasakhir", 
	                     passwd="belumselesai", 
	                     db="tugasakhir")
	cur = conn.cursor()

	@staticmethod
	def isConnect():
		MDP.cur.execute("SELECT VERSION()")
		data = MDP.cur.fetchone()
		return data

	@staticmethod
	def getQuery(_sql):
		try:
			MDP.cur.execute(_sql)
			result = []
			for res in MDP.cur.fetchall():
				result.append(res)
			return result
			MDP.conn.commit()
		except:
			return []
			MDP.conn.rollback()

	@staticmethod
	def get5w1h(ids=[]):
		ids = [str(i) for i in ids]
		res = []
		for uid in ids:
			res += MDP._get5w1h(uid)
		return res

	@staticmethod
	def _get5w1h(uid):
		que_res = MDP.getQuery(MDP._getQueryText(uid))
		res = [Info5W1H(item[0], item[1], item[2], item[3], item[4], item[5], item[6]) for item in que_res]
		return res

	@staticmethod
	def _getQueryText(uid):
		return "SELECT 5w1hs.what, 5w1hs.who, 5w1hs.when, 5w1hs.where, 5w1hs.why, 5w1hs.how, articles.text, articles.title FROM 5w1hs, articles WHERE 5w1hs.article_id = articles.id AND user_id=%s" % (uid)


