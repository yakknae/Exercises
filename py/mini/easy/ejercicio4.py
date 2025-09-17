"""Contar palabras en un texto
Dado un texto (puede estar fijo en el código), cuenta cuántas palabras contiene y muestra el resultado."""

texto = "hola como estas "
palabras = texto.split()
conteo = len(palabras)

print(f"la cantidad de palabras en el texto fueron: {conteo}")