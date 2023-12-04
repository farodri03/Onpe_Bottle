% include('_header.tpl')

<head>
  <title>Personeros</title>
</head>

<body>
  <main class="main">
    <section class="tablasP">
      <h2>Lista de Personeros</h2>
      <table>
        <thead>
          <th style="color: #fff;">id</th>
          <th style="color: #fff;">Nombres</th>
          <th style="color: #fff;">Apellidos</th>
          <th style="color: #fff;">DNI</th>
          <th style="color: #fff;">Firma</th>
          <th style="color: #fff;">Nombre del partido</th>
        </thead>
        <tbody>
          % for tp in personero:
            <tr>
              <td>{{tp[0]}}</td>
              <td>{{tp[1]}}</td>
              <td>{{tp[2]}}</td>
              <td>{{tp[3]}}</td>
              <td>
                <img src="{{tp[4]}}" alt="{{tp[1]}}" width="100">
              </td>
              <td>{{tp[5]}} </td>
            </tr>  
          % end
        </tbody>
      </table>
    </section>
  </main>
  % include('_footer.tpl')
</body>

