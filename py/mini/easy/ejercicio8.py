"""Calcular el factorial de un número
Usa un bucle para calcular el factorial de un número entero positivo (por ejemplo, 5! = 5×4×3×2×1)."""

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
numero = int(input("de que numero queres calcular el factorial?: "))
resultado = factorial(numero)
print(resultado)