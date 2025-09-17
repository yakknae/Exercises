"""Leer un archivo de texto
Lee el contenido del archivo saludo.txt creado anteriormente y muéstralo por pantalla."""

with open('hola.txt','r',encoding='utf-8') as file:
    archivo = file.read()
    print(archivo)