% include('_header.tpl')

<head>
  <title>Miembros</title>
</head>

<body>
  <main class="main">
    <section>
      <h2>Lista de Miembros</h2>
      <table>
        <thead>
          <th style="color: #fff;">Nombres</th>
          <th style="color: #fff;">Apellidos</th>
          <th style="color: #fff;">DNI</th>
          <th style="color: #fff;">Firma</th>
          <th style="color: #fff;">Nombre del cargo</th>
        </thead>
        <tbody>
          % for tp in miembros:
            <tr>
              <td>{{tp[0]}}</td>
              <td>{{tp[1]}}</td>
              <td>{{tp[2]}}</td>
              <td>
                <img src="{{tp[3]}}" alt="{{tp[1]}}" width="100">
              </td>
              <td>{{tp[4]}}</td>
            </tr>  
          % end
        </tbody>
      </table>
    </section>
  </main>
  % include('_footer.tpl')
</body>
