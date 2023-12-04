% include('_header.tpl')

<head>
  <title>Actas electorales</title>
</head>

<body>
  <main class="main">
    <section>
      <h2 class="actasTitulo">Actas Electorales</h2>
      <table class="center-table">
        <thead>
          <th style="color: #fff;">Mesa de sufragio</th>
          <th style="color: #fff;">Fecha de emisión</th>
          <th style="color: #fff;">Total de electores habiles</th>
          <th style="color: #fff;">Cédulas recibidas</th>
          <th style="color: #fff;">Observaciones</th>
          <th style="color: #fff;">Hora de Instalación</th>
          <th style="color: #fff;">Total de votos por mesa</th>
          <th style="color: #fff;">Número de cédulas no utilizadas</th>
          <th style="color: #fff;">Hora fin</th>
          <th style="color: #fff;">Direccion de la sede</th>
          <th style="color: #fff;">Departamento</th>
        </thead>
        <tbody>
          % for tp in actas:
          <tr>
            <td>{{ tp[0] }}</td>
            <td>{{ tp[1] }}</td>
            <td>{{ tp[2] }}</td>
            <td>{{ tp[3] }}</td>
            <td>{{ tp[4] }}</td>
            <td>{{ tp[5] }}</td>
            <td>{{ tp[6] }}</td>
            <td>{{ tp[7] }}</td>
            <td>{{ tp[8] }}</td>
            <td>{{ tp[9] }}</td>
            <td>{{ tp[10] }}</td>
          </tr>
          % end
        </tbody>
      </table>
    </section>
  </main>
  % include('_footer.tpl')

</body>