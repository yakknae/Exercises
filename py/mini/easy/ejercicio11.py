"""Generar la tabla de multiplicar de un número
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10."""


def multiplicar(numero,i=1):
    if i > 10:
        return 
    else:
        print(f"{numero} x {i} = {numero * i}")
        multiplicar(numero,i+1)




numero = int(input("ingrese un numero: "))

resultado = multiplicar(numero)
print(resultado)