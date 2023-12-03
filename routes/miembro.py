from bottle import Bottle, run, template, static_file, request, redirect
from sqlalchemy import text
from database import engine
sub_app = Bottle()

@sub_app.route('/', method='GET')
def miembro():
  conn = engine.connect()
  stmt = text(("""
        SELECT C.nombres,C.apellidos,C.dni,C.firma_url,CA.nombres FROM miembros M
INNER JOIN ciudadanos C ON M.ciudadano_id = C.id
INNER JOIN cargos CA ON M.cargo_id = CA.id
    """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {'miembros': rs}
  return template('miembro/index', locals)

@sub_app.route('/agregar', method='GET')
def miembro_agregar():
  locals = {'titulo': 'Agregar'}
  return template('miembro/detalle', locals)

@sub_app.route('/grabar', method='POST')
def miembro_grabar():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombres = request.forms.get('nombres')
  apellidos = request.forms.get('apellidos')
  dni = request.forms.get('dni')
  firma_url = request.forms.get('firma_url')
  nombreC = request.forms.get('nombreC')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(("""
    INSERT INTO ciudadanos (nombres, apellidos, dni, firma_url) 
    VALUES ('{}', '{}', '{}', '{}');
    INSERT INTO cargos (nombres) 
    VALUES ('{}');
    """).format(nombres, apellidos, dni, firma_url,nombreC))
  mensaje = "Miembro agregado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/miembro?mensaje=' + mensaje)