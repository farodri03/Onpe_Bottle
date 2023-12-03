% include('_header.tpl')
<h2>Lista de Personeros</h2>
<table>
  <thead>
    <th>id</th>
    <th>Nombres</th>
    <th>Apellidos</th>
    <th>DNI</th>
    <th>Firma</th>
    <th>Nombre del partido</th>
  </thead>
  <tbody>
    % for tp in personero:
      <tr>
        <td>{{tp[0]}}</td>
        <td>{{tp[1]}}</td>
        <td>{{tp[2]}}</td>
        <td>{{tp[3]}}</td>
        <td>
          <img src="{{tp[4]}}" alt="{{tp[1]}}" width="100"
        </td>
        <td>{{tp[5]}} </td>
      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')