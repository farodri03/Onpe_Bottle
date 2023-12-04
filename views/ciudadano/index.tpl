% include('_header.tpl')

<head>
  <title>Ciudadanos</title>
</head>

<body>
  <main class="main">
    <section class="tablasP">
      <h2>Lista de Ciudadanos</h2>
      <a href="/ciudadano/agregar"><button class="agregarCiudadano">Agregar Ciudadano</button></a>
      <table>
        <thead>
          <th style="color: #fff;">id</th>
          <th style="color: #fff;">Nombres</th>
          <th style="color: #fff;">Apellidos</th>
          <th style="color: #fff;">Dni</th>
          <th style="color: #fff;">Firma</th>
          <th style="color: #fff;">Acciones </th>
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
            <td>
              <a href="/ciudadano/eliminar?id={{tp[0]}}" class="button">Eliminar</a>
            </td>
          </tr>
          % end
        </tbody>
      </table>
    </section>
  </main>
  % include('_footer.tpl')
  
</body>

