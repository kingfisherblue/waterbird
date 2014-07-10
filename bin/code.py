import web
import calendar
import time
import utils

urls = (
	'/', 'index',
	'/month', 'month',
	# '/date', 'date',
	'/date/(.+)', 'date2'
	# '/date=(.+)', 'date2'
)

web.config.debug = False

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
db = web.database(dbn='mysql', user='waterbird_admin', pw='orange', db='waterbird_db')
render = web.template.render('templates/', base='layout', globals={'session': session})
calendar.setfirstweekday(calendar.SUNDAY)

class index():
	def GET(self):
		session.month = time.strftime('%m')
		session.day = time.strftime('%d')
		session.year = time.strftime('%y')
		web.seeother('/month')

class month():
	def GET(self):
		y = int(session.year)
		m = int(session.month)
		c = calendar.monthcalendar(y, m)
		return render.month(cal=c, session=session)

class date():
	def GET(self):
		d = 'Id=\'%s-%s-%s\'' % (session.year, session.month, session.day)
		e = db.select('dates', what='Body', where=d)
		return render.date(entry=e, session=session)

	def POST(self):
		e = web.input().entry.strip()
		d = time.strftime('%Y-%m-%d') 
		de = 'Id=\'%s-%s-%s\'' % (session.year, session.month, session.day)
		if db.select('dates', where=d):
			db.update('dates', where=de, body=e)
		else:
			db.insert('dates', id=d, body=e)
		raise web.seeother('/date')

class date2():
	def GET(self, params):
		date_input = params.split('-')
		year = date_input[0]
		month = date_input[1] if len(date_input[1]) == 2 else '0'+ date_input[1]
		day = date_input[2] if len(date_input[2]) == 2 else '0'+ date_input[2]

		d = 'Id=\'%s-%s-%s\'' % (year, month, day)
		e = db.select('dates', what='Body', where=d)
		session.year = year
		session.month = month
		session.day = day
		return render.date(entry=e, session=session)


if __name__ == "__main__":
	app.run()


# 'month':time.strftime('%m'), 'day':time.strftime('%d')