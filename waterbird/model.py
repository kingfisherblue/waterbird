import web

USERNAME = 'waterbird_admin'
PASSWORD = 'orange'
DBNAME = 'waterbird_db'
TABLE = 'dates'


class Model(object):

	def __init__(self, db=DBNAME):
		self.db = web.database(dbn='mysql', user=USERNAME, pw=PASSWORD, db=db)

	def getMonthEntries(self, year, month, table=TABLE):
		query = 'Id LIKE \'%04d-%02d-__\'' % (int(year), int(month))
		entries = self.db.select(table, what='Id', where=query)


	def getDateEntry(self, year, month, day, table=TABLE):
		query = 'Id=\'%s-%s-%s\'' % (year, month, day)
		entry = self.db.select(table, what='Body', where=query)
		return entry


	def updateEntry(self, text, year, month, day, table=TABLE):
		curr_dt = '%s-%s-%s' % (year, month, day)
		query = 'Id=\'%s\'' % curr_dt
		result =  self.db.select(table, where=query)
		for i in result:
			self.db.update(table, where=query, body=text)
			return

		# if no result, insert the values
		self.db.insert(table, id=curr_dt, body=text)


	def deleteEntry(self, year, month, day, table=TABLE):
		query = 'Id=\'%s-%s-%s\'' % (year, month, day)
		self.db.delete(table, where=query)


