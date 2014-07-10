import web
import calendar
from waterbird.utils import *

urls = (
	'/', 'index',
	'/month', 'month',
	'/date/(.+)', 'date',
	'/error', 'error'
)

web.config.debug = False

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
render = web.template.render('templates/', base='layout', globals={'session': session})
db = web.database(dbn='mysql', user='waterbird_admin', pw='orange', db='waterbird_db')

class index():
	def GET(self):
		setSession(session)
		web.seeother('/month')

class month():
	def GET(self):
		c = getMonthCalendar(int(session.year), int(session.month))
		return render.month(cal=c, session=session)

class date():
	def GET(self, params):
		pd = parseDateUrl(params)
		if 'day' not in pd:
			web.seeother('/error')

		year = pd['year']
		month = pd['month']
		day = pd['day']

		d = 'Id=\'%s-%s-%s\'' % (year, month, day)
		e = db.select('dates', what='Body', where=d)
		
		setSession(session, year, month, day)
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

class error():
	def GET(self):
		return render.index('Something is wrong with that url.')

if __name__ == "__main__":
	app.run()

