import MySQLdb


class MDP(object):

	def __init__(self):
		self.conn = MySQLdb.connect(host="localhost", 
		                     user="tugasakhir", 
		                     passwd="xxx", 
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

	# def getData(self, limit=0):
	# 	if (limit==0):
	# 		return self.getQuery123("SELECT * FROM clean_data")
	# 	else:
	# 		return self.getQuery123("SELECT * FROM clean_data LIMIT 0,%d" % (limit))



class TextDP(object):

	def __init__(self):
		pass

	# def getIndoWordList(self):
	# 	arr = open("indowordlists/05-ivanlanin2011-sort-alpha.lst").read().split("\n")
	# 	return arr[:len(arr)-1]

	# def getPropDescCWWordList(self):
	# 	arr = open("indowordlists/propdesc_cw.lst").read().split("\n")
	# 	return arr[:len(arr)-1]


