from bottle import Bottle, run, template, static_file, request, redirect
from sqlalchemy import text
from database import engine
sub_app = Bottle()

@sub_app.route('/', method='GET')
def miembro():
    conn = engine.connect()
    stmt = text("""
        SELECT C.nombres, C.apellidos, C.dni, C.firma_url, CA.nombres FROM miembros M
        INNER JOIN ciudadanos C ON M.ciudadano_id = C.id
        INNER JOIN cargos CA ON M.cargo_id = CA.id
    """)
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
    # crear ciudadano
    stmt_ciudadano = text("""
        INSERT INTO ciudadanos (nombres, apellidos, dni, firma_url) 
        VALUES (:nombres, :apellidos, :dni, :firma_url)
    """)
    conn.execute(stmt_ciudadano, {'nombres': nombres, 'apellidos': apellidos, 'dni': dni, 'firma_url': firma_url})

    # obtener el ID del último ciudadano insertado
    last_inserted_id = conn.execute(text("SELECT last_insert_rowid()")).scalar()

    # crear cargo solo si nombreC no es nulo
    if nombreC is not None:
        stmt_cargo = text("""
            INSERT INTO cargos (nombres) 
            VALUES (:nombreC)
        """)
        conn.execute(stmt_cargo, {'nombreC': nombreC})
    else:
        print("Error: nombreC no puede ser nulo. Handle this case accordingly.")

    mensaje = "Miembro agregado"
    conn.commit()
    conn.close()
    # redireccionar al listado
    return redirect('/miembro?mensaje=' + mensaje)