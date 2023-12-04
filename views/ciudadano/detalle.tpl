% include('_header.tpl')

<head>
  <title>Agregar ciudadano</title>
</head>

<body>
  <section>
    <div class="formCont">
      <h2 class="tituloAgregar">{{titulo}} Ciudadano</h2>
      <form class="formIns" action="/ciudadano/grabar" method="post">
        <input type="hidden" name="id" value="E"><br>
        <label for="nombre">Nombre:</label><br>
        <input type="text" name="nombres" value=""><br>
        <label for="name">Apellidos:</label><br>
        <input type="text" name="apellidos" value=""><br>
        <label for="name">DNI:</label><br>
        <input type="text" name="dni" value=""><br>
        <label for="name">Firma_url:</label><br>
        <input type="text" name="firma_url" value=""><br>
        <br><br>
        <a href="/ciudadano"><button class="btn">Atrás</button></a>
        <button class="btn">Guardar Cambios</button>
      </form>
    </div>
  </section>
</body>


% include('_footer.tpl')