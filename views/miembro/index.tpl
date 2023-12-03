% include('_header.tpl')
<h2>Lista de Miembros</h2>

<table>
  <thead>
    <th>Nombres</th>
    <th>Apellidos</th>
    <th>DNI</th>
    <th>Firma</th>
    <th>Nombre del cargo</th>
  </thead>
  <tbody>
    % for tp in miembros:
      <tr>
        <td>{{tp[0]}}</td>
        <td>{{tp[1]}}</td>
        <td>{{tp[2]}}</td>
        <td>
          <img src="{{tp[3]}}" alt="{{tp[1]}}" width="100"
        </td>
        <td>{{tp[4]}}</td>
      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')