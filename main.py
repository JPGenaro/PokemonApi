from pokemonApi import *


pokemon_name = input("Ingrese el nombre del pokemon: ")

stats = main(pokemon_name)
print(stats)
f = open('PaginaWeb.html','w')

try:
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
        <div class="container">
            <table>
                <tr>
                    <td>Nombre</td>
                    <td>{stats['name']}</td>
                </tr>
                <tr>
                    <td>Tipos</td>
                    <td>{stats['type']}</td>
                </tr>
                <tr>
                    <td>Altura</td>
                    <td>{stats['height']}</td>
                </tr>
                <tr>
                    <td>Abilidades</td>
                    <td>{stats['abilities']}</td>
                </tr>
                
                <tr>
                    <td>Peso</td>
                    <td>{stats['weight']}</td>
                </tr>
                
                
            </table>
        </div>
        
    </body>
    </html>
    """
    f.write(mensaje)
except:
    print('No se encontro el pokemon')


f.close()