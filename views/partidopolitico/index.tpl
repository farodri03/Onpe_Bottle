% include('_header.tpl')
<h2>Lista de Partidos Políticos</h2>
<p>This is a simple HTML page.</p>
<a href="/partidopolitico/agregar" class="button">Agregar Registro</a>
<table>
  <thead>
    <th>id</th>
    <th>Nombre</th>
    <th>Imagen del partido</th>

  </thead>
  <tbody>
    % for tp in partidopolitico:
      <tr>
        <td>{{tp[0]}}</td>
        <td>{{tp[1]}}</td>
        <td>
            <img src="{{tp[2]}}" alt="{{tp[1]}}" width="100"                           height="100">
        </td>
        <td>
            <a href="/partidopolitico/eliminar?id={{tp[0]}}" class="button">Eliminar</a>
        </td>
      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')