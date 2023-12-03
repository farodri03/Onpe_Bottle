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
