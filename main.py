from bottle import Bottle, run, template, static_file, request, redirect
from sqlalchemy import text
from database import engine
from routes.partidopolitico import sub_app as partidopolitico_app
from routes.ciudadano import sub_app as ciudadano_app
from routes.actaelectoral import sub_app as actaelectoral_app
from routes.miembro import sub_app as miembro_app
from routes.personero import sub_app as personero_app

app = Bottle()

# Ruta para servir archivos estáticos
@app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./views/static/css')

# Ruta de inicio
@app.route('/', method='GET')
def home():
    return template('home')

# Rutas de los subaplicativos
if __name__ == '__main__':
  app.mount('/partidopolitico', partidopolitico_app)
  app.mount('/ciudadano', ciudadano_app)
  app.mount('/actaelectoral', actaelectoral_app)
  app.mount('/miembro', miembro_app)
  app.mount('/personero', personero_app)
  try:
    run(app, host='localhost', port=8080, debug=True, reloader=True)
  except KeyboardInterrupt:
    pass
  finally:
    app.close();
