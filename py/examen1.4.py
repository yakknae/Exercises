print("bucle: ")


def sumar_bucle(valor):
    suma=0
    while (valor != 11):
        suma += valor
        print(f"{valor}")
        valor+=1
    return suma

resultado2 = sumar_bucle(1)
print(resultado2)

print("recursividad: ")

def sumar(valor):
    if valor == 10:
        return 10
    else:
        return valor + sumar(valor+1)
    
resultado = sumar(1)
print(resultado)

