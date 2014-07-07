import web

urls = (
	'/', 'index'
)

render = web.template.render('templates/', base='layout')
db = web.database(dbn='mysql', user='flora-todo', pw='', db='todo_db')

class index():
	def GET(self):
		return render.index()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()