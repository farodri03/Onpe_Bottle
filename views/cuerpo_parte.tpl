% include('_header.tpl')
<h2>Lista de Partes del Cuerpo</h2>
<p>{{mensaje}}</p>
<a href="/parte_cuerpo/agregar" class="button">Agregar Registro</a>
<table>
  <thead>
    <th>id</th>
    <th>Nombre</th>
    <th>Operciones</th>
  </thead>
  <tbody>
    % for tp in cuerpo_partes:
      <tr>
        <td>{{tp[0]}}</td>
        <td>{{tp[1]}}</td>
        <td>
          <a href="/parte_cuerpo/editar?id={{tp[0]}}" class="button">Editar</a>
          <a href="/parte_cuerpo/eliminar?id={{tp[0]}}" class="button">Eliminar</a>
        </td>
      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')