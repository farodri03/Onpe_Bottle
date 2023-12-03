% include('_header.tpl')
<h2>{{titulo}} Partes del Cuerpo</h2>
<a href="/parte_cuerpo" class="button">Atras</a>
<form action="/parte_cuerpo/grabar_editado" method="post">
  <input type="hidden" name="id" value="{{r[0]}}"><br>
  <label for="name">Nombres:</label><br>
  <input type="text" name="nombre" value="{{r[1]}}"><br>
  <br><br>
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')