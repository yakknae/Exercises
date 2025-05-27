def sumar(d):
    if d == 1:
        return 1
    else:
        return d + sumar(d-1)
    
lista = sumar(4)
print(lista)