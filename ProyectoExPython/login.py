#!/usr/bin/env -S python3

import cgi
import mysql.connector


def mostrarPaginaUsuarioNoEncontrado():
    print('Content-Type: text/html\r\n\r\n')
    print('<!DOCTYPE html>')
    print('<html lang="en">')
    print('<head>')
    print('<meta charset="UTF-8">')
    print('<title>Usuario no registrado</title>')
    print('</head>')
    print('<body>')
    print('<h1>Usuario no registrado</h1>')
    print('<p>')
    print('El usuario no se ha registrado todavía. ')
    print('<a href="/registar.html">Registrarme!</a>')
    print('</p>')
    print('</body>')
    print('</html>')


form = cgi.FieldStorage()

usuario = form['nombre']
contrasena = form['contrasena']

mi_conexion = mysql.connector.connect(host='localhost', username='www-data', password='', database='GAMES')

cur = mi_conexion.cursor()

cur.execute('SELECT id, usuario, email, tipo FROM usuario WHERE nombre = %s and contrasena= %s')
usuario_bd = cur.fetchone()

cur.close()
mi_conexion.close()

if usuario_bd == None:
    # usuario no registrado
    mostrarPaginaUsuarioNoEncontrado()
else:
    print('Set-Cookie: usuarioid='+ str(usuario_bd[0]) + ';')
    tipo = usuario_bd[3]

    if tipo.lower() == 'empleado':
        print('Location: /cgi-bin/admin.py')
    else:
        print('Location: /cgi-bin/productos.py')
