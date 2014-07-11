import unittest
from waterbird.model import *
from random import randrange
from os import system
import web

testDB = 'TestingDates'

class ModelTestCase(unittest.TestCase):
	def setUp(self):
		# create the testing database
		system('mysql -u root < /Users/florafong/Snippets/waterbird/tests/Testing.sql')
		self.db = Model(testDB)
		# self.webdb = web.database(dbn='mysql', user='root', pw='', db=testDB)
		# self.webdb.query('GRANT ALL PRIVILEGES ON waterbird_db.TestingDates TO \'waterbird_admin\'@\'localhost\'')

	def tearDown(self):
		q = 'DROP TABLES %s' % testDB
		self.webdb.query(q)

	# def suite():
	# 	return unittest.makeSuite(ModelTestCase, 'test')

	# def testUpdateEntry(self):
	# 	self.db.updateEntry('testing text', '2014', '03', '01')

	# 	q = 'SELECT COUNT(*) AS num from %s' % testDB
	# 	res = self.webdb.query(q)
	# 	assert res[0].num == 1, 'entry was not inserted correctly'


if __name__ == "__main__":
	unittest.main()