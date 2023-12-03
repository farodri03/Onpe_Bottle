% include('_header.tpl')
<h2>Lista de Ejercicios</h2>
<p>This is a simple HTML page.</p>
<a href="/ejercicio/agregar" class="button">Agregar Registro</a>
<table>
  <thead>
    <th>id</th>
    <th>Nombre</th>
    <th>Parte del Cuerpo</th>
    <th>Imagen</th>
    <th>Video</th>
  </thead>
  <tbody>
    % for ejercicio in ejercicios:
      <tr>
        <td>{{ejercicio[0]}}</td>
        <td>{{ejercicio[1]}}</td>
        <td>{{ejercicio[6]}}</td>
        <td>
          <img src="{{ejercicio[2]}}" alt="{{ejercicio[1]}}" width="100" height="100">
        </td>
        <td>
          <a href="{{ejercicio[4]}}" target="_blank" class="button">Ver Video</a>
          <a href="/ejercicio/editar?id={{ejercicio[0]}}" class="button">Editar</a>
          <a href="/ejercicio/eliminar?id={{ejercicio[0]}}" class="button">Eliminar</a>
        </td>
      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')
