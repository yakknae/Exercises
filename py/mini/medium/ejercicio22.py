"""Guardar resultados en un archivo CSV
Genera una lista de diccionarios con claves como nombre y puntuacion. Luego, guárdalos en un archivo resultados.csv."""
import csv

datos = [
    {'nombre':'valentino','nota':7},
    {'nombre':'agos','nota':1},
    {'nombre':'javier','nota':10},
]

with open('notas.csv','w',encoding='utf-8')as archivo:
    campos = ["nombre","nota"]
    yo = csv.DictWriter(archivo,fieldnames=campos)
    yo.writeheader()
    yo.writerows(datos)
