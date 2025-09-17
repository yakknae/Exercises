"""Juego: Adivina el número
El programa debe generar un número aleatorio entre 1 y 10. El usuario debe adivinarlo. El bucle continúa hasta que acierte."""

import random

random = random.randint(1,10)
intentos = 1
adivinar = int(input("adivina cual es el numero: "))

while adivinar != random:
    adivinar = int(input("adivina cual es el numero: "))
    intentos = intentos + 1

print(f"adivinaste en {intentos} intentos, el numero era {adivinar}")

