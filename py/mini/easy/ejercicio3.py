"""Leer un archivo CSV e imprimir su contenido
Crea un archivo datos.csv con columnas: nombre, edad, ciudad. Luego, escribe un programa que lo lea e imprima cada fila como un diccionario."""
import csv
with open('datos.csv','r',encoding='utf-8')as file:
    archivo = csv.reader(file)
    for line in archivo:
        print(line)