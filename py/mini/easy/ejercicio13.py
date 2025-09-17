"""Escribir en un archivo de texto
Crea un archivo llamado saludo.txt y escribe en él dos líneas de texto: una saludo y otra frase personalizada."""

with open('hola.txt','w',encoding='utf-8')as file:
    file.write("hola como estas\n")
    file.write("todo bien=?")
print("archivo creado")
