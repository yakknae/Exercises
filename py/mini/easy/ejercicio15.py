"""Jugar piedra, papel o tijera contra la computadora
El usuario elige una opción. La computadora elige aleatoriamente. Determina quién gana según las reglas del juego."""

import random
lista = ['piedra','papel','tijera']
usuario = input("elije piedra, papel o tijera: ").lower()
eleccion = random.choice(lista)

print(f"Tú: {usuario}, Computadora: {eleccion}")

if usuario == eleccion:
    print("empate")
elif (usuario == "piedra" and eleccion == "tijera") or \
     (usuario == "papel" and eleccion == "piedra") or \
     (usuario == "tijera" and eleccion == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste :(")
