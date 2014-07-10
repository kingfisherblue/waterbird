'''Adds zeroes to the front of single digits'''
def addZeroes(calendar):
	new = []
	for week in calendar:
		new_week = [x if x > 10 else '%02d' % x for x in week]
		new.append(new_week)
	return new