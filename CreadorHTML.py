from pokemonApi import *

stats = main('pikachu')
print(stats['name'])
f = open('PaginaWeb.html','w')

mensaje = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pokemon Wiki</title>

</head>

<body>
    <div class="buscador">
        <p class="search">Ingrese el nombre del pokemon a buscar</p>
        <div class="search">
            <form action="#">
                <input type="text"
                    placeholder=" Search Courses"
                    name="search">
                <button class="btn rojo" id="buttonRed" onclick="red()">Rojo</button>
            </form>
        </div>
    </div>
    <div class="container">
        <table>
            <tr>
                <td>Nombre</td>
                <td>{stats['name']}</td>
            </tr>
            <tr>
                <td>triangle</td>
                <td>better</td>
            </tr>
            <tr>
                <td>bus</td>
                <td>distant</td>
            </tr>
            <tr>
                <td>piano</td>
                <td>buffalo</td>
            </tr>
            <tr>
                <td>cross</td>
                <td>promised</td>
            </tr>
            <tr>
                <td>quietly</td>
                <td>regular</td>
            </tr>
            <tr>
                <td>climate</td>
                <td>worry</td>
            </tr>
        </table>
    </div>
</body>
</html>
"""

f.write(mensaje)
f.close()