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