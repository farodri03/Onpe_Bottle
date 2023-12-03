from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine

sub_app = Bottle()


@sub_app.route('/', method='GET')
def ciudadano():
  conn = engine.connect()
  stmt = text(("""
        SELECT * FROM ciudadanos;
    """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {'ciudadanos': rs}
  return template('ciudadano/index', locals)

@sub_app.route('/agregar', method='GET')
def ciudadano_agregar():
  locals = {'titulo': 'Agregar'}
  return template('ciudadano/detalle', locals)

@sub_app.route('/grabar', method='POST')
def ciudadano_grabar():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombres = request.forms.get('nombres')
  apellidos = request.forms.get('apellidos')
  dni = request.forms.get('dni')
  firma_url = request.forms.get('firma_url')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(("""
    INSERT INTO ciudadanos (nombres, apellidos, dni, firma_url) 
    VALUES ('{}', '{}', '{}', '{}');
    """).format(nombres, apellidos, dni, firma_url))
  mensaje = "Ciudadano agregado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/ciudadano?mensaje=' + mensaje)

@sub_app.route('/eliminar', method='GET')
def ciudadano_eliminar():
  # recepcionar parametro
  id = request.params.id
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  stmt = text(("DELETE FROM ciudadanos WHERE id = {}").format(id))
  mensaje = "ciudadano eliminado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/ciudadano?mensaje=' + mensaje)