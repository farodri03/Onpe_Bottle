% include('_header.tpl')
<h2>{{titulo}} Ciudadano</h2>
<a href="/ciudadano" class="button">Atras</a>
<form action="/ciudadano/grabar" method="post">
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
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')