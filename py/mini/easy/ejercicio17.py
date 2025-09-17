"""Calcular el área de un círculo
Pide al usuario el radio de un círculo y calcula su área usando la fórmula: área = π × r². Usa math.pi para mayor precisión."""

import math
radio = float(input("ingrese el radio de un circulo: "))

pi = math.pi

resultado = (pi * (radio * radio))

print(f"El área del círculo es: {resultado:.2f}")


