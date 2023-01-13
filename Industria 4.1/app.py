import web

urls = (
    '/', 'Index', 
    '/bienvenida', 'Bienvenida'
)

app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Bienvenida:
    def GET(self):
        num1 = 10
        num2 = 15
        suma = num1 + num2
        return render.bienvenida(suma)
        #return render.bienvenida("Si funciona")
if __name__ == "__main__":
    app.run()
