from bottle import Bottle, run, template, static_file, request, redirect
from sqlalchemy import text
from database import engine
from routes.parte_cuerpo import sub_app as parte_cuerpo_app
from routes.nivel import sub_app as nivel_app
from routes.ejercicio import sub_app as ejercicio_app
from routes.partidopolitico import sub_app as partidopolitico_app
from routes.ciudadano import sub_app as ciudadano_app

app = Bottle()

# Ruta para servir archivos estáticos
@app.route('/:filename#.*#')
def send_static(filename):
  return static_file(filename, root='./views/static')


# Ruta de inicio
@app.route('/', method='GET')
def home():
  locals = {}  # {'title': 'Home'}
  return template('home', locals)


# Rutas existentes
@app.route('/medio_pago', method='GET')
def medio_pago():
  conn = engine.connect()
  stmt = text(("""
        SELECT * FROM medio_pagos;
    """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {'medio_pagos': rs}
  return template('medio_pago', locals)


@app.route('/hola', method='GET')
def hola():
  return template('hola')


# Rutas de los subaplicativos
if __name__ == '__main__':
  app.mount('/parte_cuerpo', parte_cuerpo_app)
  app.mount('/nivel', nivel_app)
  app.mount('/ejercicio', ejercicio_app)
  app.mount('/partidopolitico', partidopolitico_app)
  app.mount('/ciudadano', ciudadano_app)
  try:
    run(app, host='localhost', port=8080, debug=True, reloader=True)
  except KeyboardInterrupt:
    pass
  finally:
    app.close()
    
