from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine

sub_app = Bottle()


@sub_app.route('/', method='GET')
def partidopolitico():
  conn = engine.connect()
  stmt = text(("""
        SELECT * FROM partidos_politicos;
    """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {'partidopolitico': rs}
  return template('partidopolitico/index', locals)

@sub_app.route('/agregar', method='GET')
def partidopolitico_agregar():
  locals = {'titulo': 'Agregar'}
  return template('partidopolitico/detalle', locals)

@sub_app.route('/grabar', method='POST')
def partidopolitico_grabar():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombres = request.forms.get('nombres')
  imagen_url = request.forms.get('imagen_url')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(("""
    INSERT INTO partidos_politicos (nombres, imagen_url) 
    VALUES ('{}','{}');
    """).format(nombres, imagen_url))
  mensaje = "Ciudadano agregado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/partidopolitico?mensaje=' + mensaje)

@sub_app.route('/eliminar', method='GET')
def partidopolitico_eliminar():
  # recepcionar parametro
  id = request.params.id
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  stmt = text(("DELETE FROM partidos_politicos WHERE id = {}").format(id))
  mensaje = "Partido politico eliminado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/partidopolitico?mensaje=' + mensaje)