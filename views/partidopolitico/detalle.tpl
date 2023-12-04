% include('_header.tpl')

<head>
  <title>Agregar partido político</title>
</head>

<body>
  <section class="agregarContenido">
    <div class="formCont">
      <h2 class="tituloAgregar">{{titulo}} Partido Político</h2>
      <form class="formIns" action="/partidopolitico/grabar" method="post">
        <input type="hidden" name="id" value="E"><br>

        <label for="nombre">Nombre:</label><br>

        <input type="text" name="nombres" value=""><br>

        <label for="name">URL de la imagen:</label><br>

        <input type="text" name="imagen_url" value=""><br>
        <br><br>
        <a href="/partidopolitico"><button class="btn">Atrás</button></a>
        <button class="btn">Guardar Cambios</button>
      </form>
    </div>
  </section>
</body>

% include('_footer.tpl')