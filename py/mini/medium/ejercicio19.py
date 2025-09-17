"""Función que devuelve si un año es bisiesto
Escribe una función que reciba un año y devuelva True si es bisiesto, False si no lo es.
Condición: divisible entre 4, pero no entre 100, a menos que también sea divisible entre 400."""

año = int(input("ingrese un año: "))

if año % 4 == 0:
    print(f"{año} es un año bisiesto")
else:
    print("no es un año bisiesto")