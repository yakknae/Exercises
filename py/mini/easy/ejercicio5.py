"""Convertir grados Celsius a Fahrenheit
Escribe una función que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit usando la fórmula: F = (C × 9/5) + 32."""

celcius = input("ingrese los grados celcius que quieres convertir a fahrenheit: ")

fahrenheit = ((int(celcius)*9)/5)+32
print(f"{celcius} grados celcius equivalen a {fahrenheit} fahrenheit")