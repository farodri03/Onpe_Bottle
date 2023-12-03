from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine

sub_app = Bottle()

@sub_app.route('/', method='GET')
def personero():
  conn = engine.connect()
  stmt = text(("""
        SELECT P.id, C.nombres, C.apellidos, C.dni, C.firma_url, PP.nombres FROM personeros P
INNER JOIN ciudadanos C ON P.ciudadano_id = C.id
INNER JOIN partidos_politicos PP ON p.partido_politico_id = PP.id
    """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {'personero': rs}
  return template('personero/index', locals)
