import web
import calendar
from web import form
from waterbird.utils import *
from waterbird.model import Model
from waterbird.month import Month
from waterbird.date import Date

urls = (
	'/', 'index',
	'/month', 'month',
	'/prev', 'prev',
	'/next', 'next',
	'/date', 'date',
	'/error', 'error',
	'/login', 'login',
	'/entries', 'entries'
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
	def GET(self):
		pd = parseDateUrl(web.input().date)
		if pd == False or 'day' not in pd:
			web.seeother('/error')

		year = pd['year']
		month = pd['month']
		day = pd['day']
		setSession(session, year, month, day)

		date_obj = Date(session.year, session.month, session.day)
		if not date_obj.hasEntry:
			date_obj.hasEntry = True
			date_obj.entry = ''  # dummy entry for div to show up

		da = render.date(days=[date_obj])
		return render.layout(da, '..')


	def POST(self):
		entry = web.input().entry.strip()
		date_obj = Date(session.year, session.month, session.day)
		date_obj.updateEntry(entry)
		same = '/date?date=%s-%s-%s' % (session.year, session.month, session.day)
		raise web.seeother(same)

class login():
	def GET(self):
		lform = form.Form(
			form.Textbox('Username:'),
			form.Textbox('Password:'))

		return render.layout(render.login(form=lform))

	def POST(self):
		return 'POST'

class entries():
	def GET(self):
		month = Month(int(session.year), int(session.month))
		da = render.date(days=month.days)

		return render.layout(da, '..')

class error():
	def GET(self):
		return render.index('Something is terribly wrong.')

if __name__ == "__main__":
	app.run()

