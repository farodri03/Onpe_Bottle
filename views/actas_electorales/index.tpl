% include('_header.tpl')
<h2>Actas Electorales</h2>
<p>This is a simple HTML page.</p>
<a href="/actaelectoral/agregar" class="button">Agregar Registro</a>
<table>
  <thead>
    <th>Mesa de sufragio</th>
    <th>Fecha de emisión</th>
    <th>Total de electores habiles</th>
    <th>Cédulas recibidas</th>
    <th>Observaciones</th>
    <th>Hora de Instalación</th>
    <th>Total de votos por mesa</th>
    <th>Número de cédulas no utilizadas</th>
    <th>Hora fin</th>
    <th>Direccion de la sede</th>
    <th>Departamento</th>
  </thead>
  <tbody>
    % for tp in actas:
      <tr>
        <td>{{tp[0]}}</td>
        <td>{{tp[1]}}</td>
        <td>{{tp[2]}}</td>
        <td>{{tp[3]}}</td>
        <td>{{tp[4]}}</td>
        <td>{{tp[5]}}</td>
        <td>{{tp[6]}}</td>
        <td>{{tp[7]}}</td>
        <td>{{tp[8]}}</td>
        <td>{{tp[9]}}</td>
        <td>{{tp[10]}}</td>

      </tr>  
    % end
  </tbody>
</table>
% include('_footer.tpl')
