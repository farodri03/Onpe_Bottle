% include('_header.tpl')
<h2>{{titulo}} Miembro</h2>
<a href="/miembro" class="button">Atras</a>
<form action="/miembro/grabar" method="post">
  <input type="hidden" name="id" value="E"><br>
  <label for="nombre">Nombres:</label><br>
  <input type="text" name="nombres" value=""><br>
  <label for="name">Apellidos:</label><br>
  <input type="text" name="apellidos" value=""><br>
  <label for="name">DNI:</label><br>
  <input type="text" name="dni" value=""><br>
  <label for="name">DNI:</label><br>
  <input type="text" name="dni" value=""><br>
  <label for="name">Firma url:</label><br>
  <input type="text" name="firma_url" value=""><br>
  <label for="name">Cargo:</label><br>
  <input type="text" name="cargo" value=""><br>

  <br><br>
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')