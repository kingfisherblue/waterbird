import unittest
from waterbird.utils import *
from random import randrange

class UtilsTestCase(unittest.TestCase):
	def suite():
		return unittest.makeSuite(UtilsTestCase, 'test')

	def testParseDateUrl(self):
		year = randrange(1000,9999)
		month = randrange(1,13)
		day = randrange(1,31)  # kind of risky...

		url = '%d-%d-%d' % (year, month, day)
		res = parseDateUrl(url)
		assert int(res['year']) == year, 'year was parsed incorrectly'
		assert int(res['month']) == month, 'month was parsed incorrectly'
		assert int(res['day']) == day, 'day was parsed incorrectly'


if __name__ == "__main__":
	unittest.main()
	