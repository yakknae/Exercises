"""Verificar si una palabra es palíndromo
Escribe un programa que determine si una palabra ingresada por el usuario se lee igual al derecho que al revés (como "reconocer")."""

palabra = input("ingrese una palabra: ")
palabra.strip().lower()
reverse = ''.join(reversed(palabra))

#caso 1
if palabra == reverse:
    print(f"la palabra '{palabra}' es palíndromo")
else:
    print(f"la palabra '{palabra}' no es palíndromo")

#caso 2
if palabra == palabra[::-1]:
    print(f"la palabra '{palabra}' es palíndromo")
else:
    print(f"la palabra '{palabra}' no es palíndromo")