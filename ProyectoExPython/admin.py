#!/usr/bin/env -S python3

import os
import cgi
import mysql.connector
import comun

def mostrarPaginaAdmin(infoUsuario):
    print('Content-Type: text/html\n\n')
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('<head>')
    print('<meta charset="UTF-8">')
    print('<title>Usuario no registrado</title>')
    print('<link rel="stylesheet" href="/stilos.css">')
    print('</head>')
    print('<body>')

    # TODO: Cambiar por la info correcta del usuario identificado
    comun.mostrarBarraNavegacion(infoUsuario)

    print('</body>')
    print('</html>')

cookies = comun.getCookies()
if not 'usuarioid' in cookies or cookies['usuarioid'] == '':
    comun.redirect('/index.html')

else:
    usuario_id = int(cookies['usuarioid'])

    mi_conexion = comun.crearConexionBD()
    cur = mi_conexion.cursor()
    cur.execute('SELECT id, usuario, email, tipo, avatar FROM usuario WHERE usuarioid= %s', (usuario_id))
    usuario_bd = cur.fetchone()
    cur.close()

    tipo = usuario_bd[3]
    if usuario_bd == None:
        comun.redirect("/index.html")
    elif not tipo == 'empleado':
        comun.redirect('/productos.py')
    else:
        mostrarPaginaAdmin(())
