import calendar
import sys
from waterbird.date import Date

class Month(object):
	def __init__(self, year, month):
		self.year = year
		self.month = month
		self.days = []
		self.initMonth()

	def initMonth(self):
		calendar.setfirstweekday(calendar.SUNDAY)
		day_list = calendar.monthcalendar(self.year, self.month)

		for week in day_list:
			for day in week:
				if day != 0:
					new_date = Date(self.year, self.month, int(day))
				else:
					new_date = False
				self.days.append(new_date)

if __name__ == "__main__":
	script, year, month = sys.argv
	m = Month(int(year), int(month))
	for day in m.days:
		if day:
			day.printDate()
		else:
			print day
