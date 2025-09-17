"""Convertir minutos a horas y minutos
Pide al usuario una cantidad de minutos y conviértela en horas y minutos restantes (por ejemplo: 130 minutos → 2 horas y 10 minutos)."""

minutos = int(input("ingre unos minutos: "))

hora = (minutos // 60)
minutos = (minutos % 60)

print(f"{minutos} equivales a: {hora} y {minutos} minutos")

