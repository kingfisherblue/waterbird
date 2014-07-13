import web
import calendar
from waterbird.utils import *
from waterbird.model import Model

urls = (
	'/', 'index',
	'/month', 'month',
	'/prev', 'prev',
	'/next', 'next',
	'/date/(.+)', 'date',
	'/error', 'error'
)

web.config.debug = False

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
globals = {'calmonth': calendar.month_name, 'session':session}
render = web.template.render('templates/', globals=globals)
db = Model()

class index():
	def GET(self):
		setSession(session)
		web.seeother('/month')

class month():
	def GET(self):
		c = getMonthCalendar(int(session.year), int(session.month))
		mon = render.month(cal=c)
		return render.layout(content=mon)

class prev():
	def GET(self):
		setPrev(session)
		return web.seeother('/month')

class next():
	def GET(self):
		setNext(session)
		return web.seeother('/month')

class date():
	def GET(self, params):
		pd = parseDateUrl(params)
		if pd == False or 'day' not in pd:
			web.seeother('/error')

		year = pd['year']
		month = pd['month']
		day = pd['day']
		setSession(session, year, month, day)

		entry = db.getDateEntry(year, month, day)
		da = render.date(entry=entry)
		return render.layout(da, '..')


	def POST(self, url):
		entry = web.input().entry.strip()
		db.updateEntry(entry, session.year, session.month, session.day)
		same = '/date/%s-%s-%s' % (session.year, session.month, session.day)
		raise web.seeother(same)

class error():
	def GET(self):
		return render.index('Something is wrong.')

if __name__ == "__main__":
	app.run()

