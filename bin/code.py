import web
import calendar
from waterbird.utils import *
from waterbird.model import Model
from waterbird.month import Month
from waterbird.date import Date

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

# Session will be all INTEGERS
# No more left padding

class index():
	def GET(self):
		setSession(session)
		web.seeother('/month')

class month():
	def GET(self):
		month = Month(int(session.year), int(session.month))
		month_page = render.month(month=month)
		return render.layout(content=month_page)

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

		date_obj = Date(session.year, session.month, session.day)
		da = render.date(entry=date_obj.entry)

		return render.layout(da, '..')


	def POST(self, url):
		entry = web.input().entry.strip()
		date_obj = Date(session.year, session.month, session.day)
		date_obj.updateEntry(entry)
		same = '/date/%s-%s-%s' % (session.year, session.month, session.day)
		raise web.seeother(same)

class error():
	def GET(self):
		return render.index('Something is terribly wrong.')

if __name__ == "__main__":
	app.run()

