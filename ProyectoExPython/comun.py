import os
import mysql.connector

def mostrarBarraNavegacion(usuario):
    # TODO: Cambiar por las posiciones correctas
    imagen = usuario[0]
    nombre = usuario[1]
    username = usuario[2]

    print('<div id="barra-navegacion">')
    print('<div id="home"><a href="/index.html">GAMES</a></div>')
    print('<div id="info-usuario">')
    print('<img src="{}" alt="avatar"> {} ({})'.format(imagen, nombre, username))
    print('</div>')
    print('</div>')

def redirect(pagina):
    print('Location: ' + pagina + '\n\n')

def getCookies():
    cookies = {}
    if 'HTTP_COOKIE' in os.environ:
        cookie_string = os.environ.get('HTTP_COOKIE')
        cookies_splited = cookie_string.split(';')
        for valor in cookies_splited:
            valor_splited = valor.split('=')
            cookies[valor_splited[0]] = valor_splited[1]
    return cookies

def crearConexionBD():
    return mysql.connector.connect(host='localhost', username='www-data', password='', database='GAMES')