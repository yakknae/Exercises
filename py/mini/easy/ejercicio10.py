"""Sumar elementos de una lista
Crea una lista de números y calcula la suma total de sus elementos sin usar funciones avanzadas (aunque puedes usar sum() después como variante)."""

lista = [1,2,3,4,5,6]
suma = 0

for numero in lista:
    suma += numero
 
print(f"la suma de toda la lista es {suma}")