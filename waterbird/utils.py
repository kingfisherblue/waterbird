import time
import calendar
import sys

# Class for taking care of time conversions and parsing methods 

def intToMonth(i):
	return calendar.month_name[i]

def setSession(session, y = time.strftime('%Y'), m = time.strftime('%m'), d = time.strftime('%d')):
	session.month = m
	session.day = d
	session.year = y
	session.curr_month = m
	session.curr_day = d
	session.curr_year = y

def setNext(session):
	if int(session.month) == 12:
		session.year = '%d' % (int(session.year) + 1)
		session.month = '%d' % 1
	else:
		session.month = int(session.month) + 1

def setPrev(session):
	if int(session.month) == 1:
		session.year = '%d' % (int(session.year) - 1)
		session.month = '%d' % 12
	else:
		session.month = int(session.month) - 1

def getMonthCalendar(year, month):
	calendar.setfirstweekday(calendar.SUNDAY)
	return calendar.monthcalendar(year, month)

''' Parses string of format YYYY-MM-DD or YYYY-MM. Returns dictionary \
	ex. '2014-07-01' becomes {'year': '2014', 'month':'07', 'day':'01'} '''
def parseDateUrl(url):
	result = {}
	try:
		time_s = time.strptime(url,'%Y-%m-%d')
		result['day'] = '%02d' % time_s.tm_mday
	except ValueError, TypeError:
		try:
			time_s = time.strptime(url,'%Y-%m')
		except ValueError, TypeError:
			return False

	result['year'] = time_s.tm_year
	result['month'] = '%02d' % time_s.tm_mon
	return result


if __name__ == "__main__":
	script, arg = sys.argv
	print parseDateUrl(arg)
