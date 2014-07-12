import unittest
from waterbird.utils import *
from random import randrange

class UtilsTestCase(unittest.TestCase):
	def suite():
		return unittest.makeSuite(UtilsTestCase, 'test')

	def testParseDateUrlGood(self):
		year = randrange(1000,9999)
		month = randrange(1,13)
		day = randrange(1,31)  # kind of risky...

		url = '%d-%d-%d' % (year, month, day)
		res = parseDateUrl(url)
		assert int(res['year']) == year, 'year was parsed incorrectly'
		assert int(res['month']) == month, 'month was parsed incorrectly'
		assert int(res['day']) == day, 'day was parsed incorrectly'

		url = '%d-%d' % (year, month)
		res = parseDateUrl(url)
		assert int(res['year']) == year, 'year was parsed incorrectly'
		assert int(res['month']) == month, 'month was parsed incorrectly'

		url = '2014-01-5'
		res = parseDateUrl(url)
		assert int(res['year']) == 2014, 'year was parsed incorrectly'
		assert int(res['month']) == 1, 'month was parsed incorrectly'
		assert int(res['day']) == 5, 'day was parsed incorrectly'

		url = '2014-5'
		res = parseDateUrl(url)
		assert int(res['year']) == 2014, 'year was parsed incorrectly'
		assert int(res['month']) == 5, 'month was parsed incorrectly'

	def testParseDateUrlBad(self):
		url = '20314'
		assert parseDateUrl(url) == False, 'incorrect date was parsed'

		url = '2031-13-01'
		assert parseDateUrl(url) == False, 'incorrect date was parsed'

		url = '20-31-4'
		assert parseDateUrl(url) == False, 'incorrect date was parsed'

		url = '2014-3-41'
		assert parseDateUrl(url) == False, 'incorrect date was parsed'


if __name__ == "__main__":
	unittest.main()
	