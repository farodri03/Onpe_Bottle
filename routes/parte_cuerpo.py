from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine

sub_app = Bottle()

@sub_app.route('/', method='GET')
def parte_cuerpo():
  # recepcionar parametro
  mensaje = request.params.mensaje
  # acceder a db
  conn = engine.connect()
  stmt = text(("""
    SELECT * FROM cuerpo_partes;
  """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {
    'cuerpo_partes': rs,
    'mensaje': mensaje
  }
  # retorno
  return template('cuerpo_parte', locals)

@sub_app.route('/editar', method='GET')
def parte_cuerpo_editar():
  # recepcionar parametro
  id = request.params.id
  # acceder a db
  conn = engine.connect()
  stmt = text(
    ("SELECT id, nombre FROM cuerpo_partes WHERE id = {}").format(id)
  )
  rs = conn.execute(stmt).fetchone()
  conn.close()
  locals = {'r': rs, 'titulo': 'Editar'}
  return template('cuerpo_parte_detalle_editar', locals)

@sub_app.route('/eliminar', method='GET')
def parte_cuerpo_eliminar():
  # recepcionar parametro
  id = request.params.id
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  stmt = text(
    ("DELETE FROM cuerpo_partes WHERE id = {}").format(id)
  )
  mensaje = "Parte del Cuerpo eliminada"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/parte_cuerpo?mensaje=' + mensaje)

@sub_app.route('/agregar', method='GET')
def parte_cuerpo_agregar():
  locals = {'titulo': 'Agregar'}
  return template('cuerpo_parte_detalle', locals)

@sub_app.route('/grabar_editado', method='POST')
def parte_cuerpo_grabar_editado():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombre = request.forms.get('nombre')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(
    ("UPDATE cuerpo_partes SET nombre = '{}' WHERE id = {}").format(
      nombre, id))
  mensaje = "Parte del Cuerpo editada"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/parte_cuerpo?mensaje=' + mensaje)

@sub_app.route('/grabar', method='POST')
def parte_cuerpo_grabar():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombre = request.forms.get('nombre')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(
    ("INSERT INTO cuerpo_partes (nombre) VALUES ('{}')").format(
      nombre))
  mensaje = "Parte del Cuerpo agregada"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/parte_cuerpo?mensaje=' + mensaje)
