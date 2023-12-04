% include('_header.tpl')

<head>
  <title>Niveles</title>
</head>

<h2>Lista de Niveles</h2>
<p>{{mensaje}}</p>
<a href="/nivel/agregar" class="button">Agregar Registro</a>
<table>
  <thead>
    <th style="color: #fff;">id</th>
    <th style="color: #fff;">Nombre</th>
    <th style="color: #fff;">Operciones</th>
    <th style="color: #fff;"> Acciones </th>
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