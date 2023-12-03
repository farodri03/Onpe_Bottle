from bottle import Bottle, run, template, static_file, request, redirect
from sqlalchemy import text
from database import engine
sub_app = Bottle()
@sub_app.route('/miembros', method='GET')
def miembro():
  conn = engine.connect()
  stmt = text(("""
        SELECT * FROM miembros;
    """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {'miembros': rs}
  return template('miembro', locals)

