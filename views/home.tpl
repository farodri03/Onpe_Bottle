%include('_headerH.tpl')
<head>
    <script src="/static/js/app.js"></script>
    <script src="/static/js/particles.js"></script>
    <title>Home</title>
</head>

<body>
    <header class="header" id="header">
        <nav class="navBar">
            <ul class="list_nav">
                <li class="items_nav">
                    <a href="/">Home</a>
                </li>

                <li class="items_nav">
                    <a href="/partidopolitico" class="nav_link">Partidos Políticos</a>
                </li>

                <li class="items_nav">
                    <a href="/ciudadano" class="nav_link">Ciudadanos</a>
                </li>

                <li class="items_nav">
                    <a href="/miembro" class="nav_link">Miembros</a>
                </li>

                <li class="items_nav">
                    <a href="/personero" class="nav_link">Personeros</a>
                </li>

                <li class="items_nav">
                    <a href="/actaelectoral" class="nav_link">Actas electorales</a>
                </li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="portadaHome">
            <div class="contenido">
                <img src="/static/img/logOnpe.png" alt="logo">
                <h1 id="onpePro">CARTILLAS DE MIEMBROS DE MESA</h1>
                <div id="particles"></div>
                
            </div>
        </section>

        <section class="acercaDe">
            <div class="acercaImagen">
                <img src="/static/img/AuOnpe.png" alt="logo">
            </div>
            <div class="acercaContenido">
                <h2 class="heading">About<span>Us</span></h2>
                <p>Velar por la obtención de la fiel y libre expresión de la voluntad popular de los ciudadanos, organizaciones políticas, instituciones públicas, privadas y de la sociedad civil, en todos los procesos electorales, de referéndum y otros tipos de consulta popular de manera oportuna, transparente con un enfoque intercultural e inclusivo.</p>
                <a href="https://www.web.onpe.gob.pe/home/" target="_blank"><button class="btn">Leer más</button></a>
            </div>
        </section>
    </main>

    <footer>
        <p class="footerStyle">&copy; 2023 Ing. de Datos. All rights reserved.</p>
        <p class="footerStyle">Designed by <a class="linkPerf" href="https://github.com/farodri03" target="_blank"
                style="text-decoration: none !important;">Fabian Rodriguez</a></p>
    </footer>
</body>