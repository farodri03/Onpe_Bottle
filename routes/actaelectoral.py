from bottle import Bottle, template, request, redirect
from sqlalchemy import text
from database import engine
import json

sub_app = Bottle()

@sub_app.route('/', method='GET')
def acta_electoral():
  conn = engine.connect()
  # listar ejercicios
  stmt = text(("""
    SELECT AE.num_mesa_sufragio, AE.fecha_emision, AE.total_electores_habiles, AI.celula_recibidas, AI.observacion, AI.hora_instalacion, ASU.total_votos_ciudadanos,
ASU.num_celulas_no_utilizadas,ASU.hora_fin,LV.direccion, DP.nombre FROM actas_electorales AE 
    INNER JOIN actas_instalaciones AI ON AE.acta_instalacion_id = AI.id 
    INNER JOIN actas_sufragios ASU ON AE.actas_sufragio_id = ASU.id 
    INNER JOIN lugares_votaciones LV ON AE.lugar_votacion_id = LV.id
  INNER JOIN distritos D ON LV.distrito_id=D.id
  INNER JOIN provincias P ON D.provincia_id = P.id
  INNER JOIN departamentos DP ON P.departamento_id = DP.id
    ORDER BY AE.num_mesa_sufragio ASC
  """).format())
  ejercicios = conn.execute(stmt)
  locals = {'actas': ejercicios}
  return template('actas_electorales/index', locals)

@sub_app.route('/agregar', method='GET')
def acta_electoral_agregar():
  locals = {'titulo': 'Agregar'}
  return template('actas_electorales/detalle', locals)
