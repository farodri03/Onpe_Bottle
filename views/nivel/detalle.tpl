% include('_header.tpl')
<h2>{{titulo}} Niveles</h2>
<a href="/nivel" class="button">Atras</a>
<form action="/nivel/grabar" method="post">
  <input type="hidden" name="id" value="E"><br>
  <label for="name">Nombres:</label><br>
  <input type="text" name="nombre" value=""><br>
  <br><br>
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')