from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine

sub_app = Bottle()


@sub_app.route('/personero', method='GET')
def personero():
  conn = engine.connect()
  stmt = text(("""
        SELECT * FROM personeros;
    """).format())
  rs = conn.execute(stmt)
  conn.close()
  locals = {'personero': rs}
  return template('personero', locals)