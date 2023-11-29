#!/usr/bin/env -S python3

import comun

def mostrarPaginaProductos(infoUsuario):
    print('Content-Type: text/html\n\n')
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('<head>')
    print('<meta charset="UTF-8">')
    print('<title>Usuario no registrado</title>')
    print('<link rel="stylesheet" href="/stilos.css">')
    print('</head>')
    print('<body>')

    mi_conexion = comun.crearConexionBD()
    cur = mi_conexion.cursor()
    cur.execute('SELECT id, usuario, email, tipo, avatar FROM usuario WHERE usuarioid= %s', (usuario_id))
    usuario_bd = cur.fetchone()
    
    # TODO: Cambiar por la info correcta del usuario identificado
    comun.mostrarBarraNavegacion(infoUsuario)

    # Mostrar los productos
    print('<section id="productos">')
    print('<h2>Productos</h2>')
    print('<ul id="lista-productos">')
    cur.execute("SELECT id, nombre, categoria, precio FROM producto ORDER BY categoria, nombre")

    for producto in cur:
        id_producto = producto[0]
        nombre = producto[1]
        precio = producto[3]
        print('<li><div class="nombre">{}</div><div class="precio">{}</div><div class="boton"><a href="/cgi-bin/agregarproducto.py?id={}>Agregar</a></div></li>'.format(nombre, precio, id_producto))

    
    print('</ul>')
    print('</section>')
    print('</body>')
    print('</html>')
    
    cur.close()
    mi_conexion.close()

cookies = comun.getCookies()
if not 'usuarioid' in cookies or cookies['usuarioid'] == '':
    comun.redirect('/index.html')
else:
    usuario_id = int(cookies['usuarioid'])

    