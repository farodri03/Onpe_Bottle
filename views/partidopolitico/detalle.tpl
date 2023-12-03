% include('_header.tpl')
<h2>{{titulo}} Partido Político</h2>
<a href="/partidopolitico" class="button">Atras</a>
<form action="/partidopolitico/grabar" method="post">
  <input type="hidden" name="id" value="E"><br>
  <label for="nombre">Nombre:</label><br>
  <input type="text" name="nombres" value=""><br>
  <label for="name">URL de la imagen:</label><br>
  <input type="text" name="imagen_url" value=""><br>
  <br><br>
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')