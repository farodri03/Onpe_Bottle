% include('_header.tpl')
<h2>{{titulo}} Ejercicio</h2>
<a href="/ejercicio" class="button">Atras</a>
<form action="/ejercicio/grabar" method="post">
  <input type="hidden" name="id" value="E"><br>
  <label for="nombre">Nombre:</label><br>
  <input type="text" name="nombre" value=""><br>
  <label for="name">Imagen URL:</label><br>
  <input type="text" name="imagen_url" value=""><br>
  <label for="name">Video URL:</label><br>
  <input type="text" name="video_url" value=""><br>
  <label for="name">Parte del Cuerpo:</label><br>
  <select name="cuerpo_parte_id">
    % for tp in cuerpo_partes:
      <option value="{{tp[0]}}">{{tp[1]}}</option>
    % end
  </select>
  <br><br>
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')