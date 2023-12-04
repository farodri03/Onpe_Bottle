% include('_header.tpl')

<head>
  <title>Partidos políticos</title>
</head>

<body>
  <main class="main">
    <section>
      <h2>Lista de Partidos Políticos</h2>
      <a href="/partidopolitico/agregar"><button class="agregarPartido">Agregar Partido</button></a>
      <table>
        <thead>
          <th style="color: #fff;">id</th>
          <th style="color: #fff;">Nombre</th>
          <th style="color: #fff;">Imagen del partido</th>
          <th style="color: #fff;"> Acciones </th>
        </thead>
        <tbody>
          % for tp in partidopolitico:
            <tr>
              <td>{{tp[0]}}</td>
              <td>{{tp[1]}}</td>
              <td>
                  <img src="{{tp[2]}}" alt="{{tp[1]}}" width="100"height="100">
              </td>
              <td>
                  <a href="/partidopolitico/eliminar?id={{tp[0]}}" class="button">Eliminar</a>
              </td>
            </tr>  
          % end
        </tbody>
      </table>
    </section>
  </main>
  % include('_footer.tpl')
</body>

