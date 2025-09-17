"""Dibujar un árbol de Navidad con asteriscos
Escribe un programa que imprima un triángulo hecho de asteriscos (*) de 5 filas de alto, centrado, y con un tronco (|) en la base."""

altura = 5
for i in range(1,altura+1): 
    print(' ' * (altura-i) + '*' * (2*i-1))
print(' '* (altura-1) + "|")