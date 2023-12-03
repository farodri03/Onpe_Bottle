% include('_header.tpl')
<h2>Lista de Ciudadanos</h2>
<p>This is a simple HTML page.</p>
<table>
  <thead>
    <th>id</th>
    <th>Nombres</th>
    <th>Apellidos</th>
    <th>dni</th>
    <th>firma</th>
  </thead>
  <tbody>
    % for tp in ciudadanos:
      <tr>
        <td>{{tp[0]}}</td>
        <td>{{tp[1]}}</td>
        <td>{{tp[2]}}</td>
        <td>{{tp[3]}}</td>
        <td>
            <img src="{{tp[4]}}" alt="{{tp[1]}}" width="100" height="100">
        </td>

      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')