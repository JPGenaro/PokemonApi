from pokemonApi import *

stats = main('pikachu')

f = open('PaginaWeb.html','w')

mensaje = f"""
<html>
<head></head>
<body><p>{stats}</p></body>
</html>"""

f.write(mensaje)
f.close()