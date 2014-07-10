import time
import calendar
import code
import sys

# Class for taking care of time conversions and parsing methods 

class DateFormatError(Exception):
    def __init__(self):
    	self.msg = 'The date is malformed.'

'''Adds zeroes to the front of single digits'''
def addZeroes(calendar):
	new = []
	for week in calendar:
		new_week = [x if x > 10 else '%02d' % x for x in week]
		new.append(new_week)
	return new

def getMonth():
	time.strftime('%m')

def getDay():
	time.strftime('%d')

def getYear():
	time.strftime('%Y')

def setSession(session, y = time.strftime('%Y'), m = time.strftime('%m'), d = time.strftime('%d')):
	session.month = m
	session.day = d
	session.year = y

def getMonthCalendar(year, month):
	try:
		calendar.setfirstweekday(calendar.SUNDAY)
		return calendar.monthcalendar(year, month)
	except TypeError:
		displayError('Error getting the month calendar.')

''' Parses string of format YYYY-MM-DD or YYYY-MM. Returns dictionary \
	ex. '2014-07-01' becomes {'year': '2014', 'month':'07', 'day':'01'} '''
def parseDateUrl(url):
	result = {}
	try:
		time_s = time.strptime(url,'%Y-%m-%d')
		result['day'] = '%02d' % time_s.tm_mday
	except ValueError:
		try:
			time_s = time.strptime(url,'%Y-%m')
		except ValueError:
			displayError('Malformed date.')

	result['year'] = time_s.tm_year
	result['month'] = '%02d' % time_s.tm_mon
	return result


def displayError(msg):
	print msg
	return code.render.index(msg)


if __name__ == "__main__":
	script, arg = sys.argv
	print parseDateUrl(arg)
