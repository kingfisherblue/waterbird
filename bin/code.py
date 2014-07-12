import web
import calendar
from waterbird.utils import *
from waterbird.model import Model

urls = (
	'/', 'index',
	'/month', 'month',
	'/date/(.+)', 'date',
	'/error', 'error'
)

web.config.debug = False

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
globals = {'calmonth': calendar.month_name, 'session':session}
render = web.template.render('templates/', base='layout', globals=globals)
db = Model()

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
		if pd == False or 'day' not in pd:
			web.seeother('/error')

		year = pd['year']
		month = pd['month']
		day = pd['day']
		setSession(session, year, month, day)

		entry = db.getDateEntry(year, month, day)
		return render.date(entry=entry, session=session)


	def POST(self):
		entry = web.input().entry.strip()
		db.updateEntry(entry, session.year, session.month, session.day)
		raise web.seeother('/date')

class error():
	def GET(self):
		return render.index('Something is wrong.')

if __name__ == "__main__":
	app.run()

