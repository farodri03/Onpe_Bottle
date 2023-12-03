% include('_header.tpl')
<h2>Lista de Niveles</h2>
<p>{{mensaje}}</p>
<a href="/nivel/agregar" class="button">Agregar Registro</a>
<table>
  <thead>
    <th>id</th>
    <th>Nombre</th>
    <th>Operciones</th>
  </thead>
  <tbody>
    % for tp in niveles:
      <tr>
        <td>{{tp[0]}}</td>
        <td>{{tp[1]}}</td>
        <td>
          <a href="/nivel/editar?id={{tp[0]}}" class="button">Editar</a>
          <a href="/nivel/eliminar?id={{tp[0]}}" class="button">Eliminar</a>
        </td>
      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')