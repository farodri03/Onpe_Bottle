% include('_header.tpl')

<head>
  <title>Agregar miembro</title>
</head>

<body>
  <section>
    <div class="formCont">
      <h2 class="tituloAgregar">{{titulo}} Miembro</h2>
      <form class="formIns" action="/miembro/grabar" method="post">
        <input type="hidden" name="id" value="E"><br>
        <label for="nombre">Nombres:</label><br>
        <input type="text" name="nombres" value=""><br>
        <label for="name">Apellidos:</label><br>
        <input type="text" name="apellidos" value=""><br>
        <label for="name">DNI:</label><br>
        <input type="text" name="dni" value=""><br>
        <label for="name">Firma url:</label><br>
        <input type="text" name="firma_url" value=""><br>
        <label for="name">Cargo:</label><br>
        <input type="text" name="cargo" value=""><br>
        <br><br>
        <a href="/miembro"><button class="btn">Atras</button></a>
        <button class="btn">Guardar Cambios</button>
      </form>

    </div>
    <!-- <a href="/miembro" class="button">Atras</a> -->
  </section>
</body>

% include('_footer.tpl')