from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine
import json

sub_app = Bottle()


@sub_app.route('/', method='GET')
def ejercio():
  conn = engine.connect()
  # listar ejercicios
  stmt = text(("""
    SELECT * FROM ejercicios E INNER JOIN cuerpo_partes CP ON E.cuerpo_parte_id = CP.id 
    ORDER BY id DESC
  """).format())
  ejercicios = conn.execute(stmt)
  locals = {'ejercicios': ejercicios}
  return template('ejercicio/index', locals)


@sub_app.route('/json', method='GET')
def ejercio_json():
  conn = engine.connect()
  # listar ejercicios
  stmt = text(("""
    SELECT * FROM ejercicios E INNER JOIN cuerpo_partes CP ON E.cuerpo_parte_id = CP.id
  """).format())
  rpta = []
  rs = conn.execute(stmt)
  for r in rs:
    print(r)
    rpta.append({
      'id': r[0],
      'nombre': r[1],
      'imagen_url': r[2],
      'video_url': r[3],
      'parte_cuerpo_id': r[4],
    })
  return json.dumps(rpta)


@sub_app.route('/agregar', method='GET')
def ejercicio_agregar():
  # listar partes del cuerpo
  conn = engine.connect()
  stmt = text(("""
    SELECT id, nombre FROM cuerpo_partes;
  """).format())
  cuerpo_partes = conn.execute(stmt)
  locals = {'titulo': 'Agregar', 'cuerpo_partes': cuerpo_partes}
  return template('ejercicio/detalle', locals)


@sub_app.route('/grabar', method='POST')
def ejercicio_grabar():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombre = request.forms.get('nombre')
  imagen_url = request.forms.get('imagen_url')
  video_url = request.forms.get('video_url')
  cuerpo_parte_id = request.forms.get('cuerpo_parte_id')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(("""
    INSERT INTO ejercicios (nombre, imagen_url, video_url, cuerpo_parte_id) 
    VALUES ('{}', '{}', '{}', {});
    """).format(nombre, imagen_url, video_url, cuerpo_parte_id))
  mensaje = "Ejercicio agregado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/ejercicio?mensaje=' + mensaje)


@sub_app.route('/eliminar', method='GET')
def ejercicio_eliminar():
  # recepcionar parametro
  id = request.params.id
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  stmt = text(("DELETE FROM ejercicios WHERE id = {}").format(id))
  mensaje = "Ejercicio eliminado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/ejercicio?mensaje=' + mensaje)


@sub_app.route('/editar', method='GET')
def ejercicio_editar():
  # recepcionar parametro
  id = request.params.id
  conn = engine.connect()
  stmt = text(("""
    SELECT id, nombre FROM cuerpo_partes;
  """).format())
  cuerpo_partes = conn.execute(stmt)
  # acceder a db
  conn = engine.connect()
  stmt = text((
    "SELECT id, nombre, imagen_url, video_url, cuerpo_parte_id FROM ejercicios WHERE id = {}"
  ).format(id))
  rs = conn.execute(stmt).fetchone()
  conn.close()
  locals = {'r': rs, 'titulo': 'Editar', 'cuerpo_partes': cuerpo_partes}
  return template('ejercicio/detalle_editar', locals)


@sub_app.route('/grabar_editado', method='POST')
def nivel_grabar_editado():
  # recepcionar datos del formulario
  id = request.forms.get('id')
  nombre = request.forms.get('nombre')
  imagen_url = request.forms.get('imagen_url')
  video_url = request.forms.get('video_url')
  cuerpo_parte_id = request.forms.get('cuerpo_parte_id')
  # acceder a la db
  conn = engine.connect()
  mensaje = ""
  # crear
  stmt = text(("""
    UPDATE ejercicios 
    SET nombre = '{}', imagen_url = '{}', video_url = '{}', cuerpo_parte_id = {}  
    WHERE id = {}
   """).format(nombre, imagen_url, video_url, cuerpo_parte_id, id))
  mensaje = "Nivel Editado"
  conn.execute(stmt)
  conn.commit()
  conn.close()
  # redireccionar al listado
  return redirect('/ejercicio?mensaje=' + mensaje)
