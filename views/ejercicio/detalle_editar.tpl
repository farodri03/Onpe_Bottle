% include('_header.tpl')
<h2>{{titulo}} Ejercicio</h2>
<a href="/ejercicio" class="button">Atras</a>
<form action="/ejercicio/grabar_editado" method="post">
  <input type="hidden" name="id" value="{{r[0]}}"><br>
  <label for="name">Nombre:</label><br>
  <input type="text" name="nombre" value="{{r[1]}}"><br>
  <label for="name">Imagen URL:</label><br>
  <input type="text" name="imagen_url" value="{{r[2]}}"><br>
  <img src="{{r[2]}}" /> <br>
  <label for="name">Video URL:</label><br>
  <input type="text" name="video_url" value="{{r[3]}}"><br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/VDrjzssQM60?si=Hs_a8aaJh-62UWf9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<br>
  <label for="name">Partes del Cuerpo:</label><br>
  <select name="cuerpo_parte_id">
    % for tp in cuerpo_partes:
      % if r[4] == tp[0]:
        <option value="{{tp[0]}}" selected>{{tp[1]}}</option>
      % else:
        <option value="{{tp[0]}}">{{tp[1]}}</option>
      % end
    % end
  </select>
  <br><br>
  <button class="btn">Guardar Cambios</button>
</form>
% include('_footer.tpl')
