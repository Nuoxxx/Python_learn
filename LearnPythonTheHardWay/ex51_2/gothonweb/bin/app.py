import web

urls = ('/hello', 'Index')

app = web.application(urls, globals())

render = web.template.render('templates/')

# class Index(object):
#     def GET(self):
#         form = web.input(name = "Nobody",greet = None)
#         if form.greet:
#             greeting = "%s, %s" % (form.greet, form.name)
#             return render.index(greeting = greeting)
#         else:
#             return "Error: greet is required."

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name = "Nobody", greet = "Hello")
        greeting = "%s, %s" %(form.greet, form.name)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
