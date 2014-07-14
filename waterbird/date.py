import datetime
from waterbird.model import Model

class Date(object):
	def __init__(self, year, month, day):
		self.date_t = datetime.date(year, month, day)
		self.hasEntry = False
		self.entry = None
		self.checkForEntry()

	def checkForEntry(self):
		db = Model()
		entry = db.getDateEntry(self.date_t.year, self.date_t.month, self.date_t.day)
		for i in entry:
			self.hasEntry = True
			self.entry = i.Body

	def updateEntry(self, entry):
		db = Model()
		if entry == '':
			db.deleteEntry(self.date_t.year, self.date_t.month, self.date_t.day)
		else:
			db.updateEntry(entry, self.date_t.year, self.date_t.month, self.date_t.day)

	# for testing
	def printDate(self):
		print 'Date: %d %d %d \n' % (self.date_t.year, self.date_t.month, self.date_t.day)
		if self.hasEntry:
			print 'Entry: %s' % self.entry
