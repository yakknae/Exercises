def rango(d,h):
    if d == h:
        return [10]
    else:
        return [d] + rango(d+1,h)
    
lista = rango(5,10)
print(lista)