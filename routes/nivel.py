from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine

sub_app = Bottle()

@sub_app.route('/', method='GET')
def nivel():
  # recepcionar parametro
  mensaje = request.params.mensaje
  # acceder a db
  conn = engine.connect()
  stmt = text(("""
    SELECT * FROM niveles;
  """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {
    'niveles': rs,
    'mensaje': mensaje
  }
  # retorno
  return template('nivel/index', locals)

@sub_app.route('/editar', method='GET')
def nivel_editar():
  # recepcionar parametro
  id = request.params.id
  # acceder a db
  conn = engine.connect()
  stmt = text(
    ("SELECT id, nombre FROM niveles WHERE id = {}").format(id)
  )
  rs = conn.execute(stmt).fetchone()
  conn.close()
  locals = {'r': rs, 'titulo': 'Editar'}
  return template('nivel/detalle_editar', locals)

@sub_app.route('/eliminar', method='GET')
def nivel_eliminar():
  # recepcionar parametro
  id = request.params.id
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  stmt = text(
    ("DELETE FROM niveles WHERE id = {}").format(id)
  )
  mensaje = "Nivel eliminado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/nivel?mensaje=' + mensaje)

@sub_app.route('/agregar', method='GET')
def nivel_agregar():
  locals = {'titulo': 'Agregar'}
  return template('nivel/detalle', locals)

@sub_app.route('/grabar_editado', method='POST')
def nivel_grabar_editado():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombre = request.forms.get('nombre')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(
    ("UPDATE niveles SET nombre = '{}' WHERE id = {}").format(
      nombre, id))
  mensaje = "Nivel Editado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/nivel?mensaje=' + mensaje)

@sub_app.route('/grabar', method='POST')
def nivel_grabar():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombre = request.forms.get('nombre')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(
    ("INSERT INTO niveles (nombre) VALUES ('{}')").format(
      nombre))
  mensaje = "Parte del Cuerpo agregada"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/nivel?mensaje=' + mensaje)
