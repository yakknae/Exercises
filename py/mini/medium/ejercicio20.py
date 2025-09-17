"""Contar líneas de un archivo de texto
Crea un archivo .txt con varias líneas de texto. Luego, escribe un programa que lea el archivo y cuente cuántas líneas tiene."""

cant = 0
with open('hola2.txt','r',encoding='utf-8') as file:
        for line in file:
            print(line)
            cant = cant + 1

print(f"en total tenia {cant} lineas")