import time
import calendar
import sys

# Class for taking care of time conversions and parsing methods 

def intToMonth(i):
	return calendar.month_name[i]

def setSession(session, y = time.strftime('%Y'), m = time.strftime('%m'), d = time.strftime('%d')):
	session.month = int(m)
	session.day = int(d)
	session.year = int(y)
	session.curr_month = int(time.strftime('%m'))
	session.curr_day = int(time.strftime('%d'))
	session.curr_year = int(time.strftime('%Y'))

def setNext(session):
	if int(session.month) == 12:
		session.year = session.year + 1
		session.month = 1
	else:
		session.month = session.month + 1

def setPrev(session):
	if int(session.month) == 1:
		session.year = session.year - 1
		session.month = 12
	else:
		session.month = session.month - 1

''' Parses string of format YYYY-MM-DD or YYYY-MM. Returns dictionary \
	ex. '2014-07-01' becomes {'year': 2014, 'month': 7, 'day': 1} '''
def parseDateUrl(url):
	result = {}
	try:
		time_s = time.strptime(url,'%Y-%m-%d')
		result['day'] = int(time_s.tm_mday)
	except ValueError, TypeError:
		try:
			time_s = time.strptime(url,'%Y-%m')
		except ValueError, TypeError:
			return False

	result['year'] = int(time_s.tm_year)
	result['month'] = int(time_s.tm_mon)
	return result


if __name__ == "__main__":
	script, arg = sys.argv
	print parseDateUrl(arg)
