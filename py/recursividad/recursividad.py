def rangoHasta(n):
    if n == 0:
        return [0]
    else:
        return rangoHasta(n-1) + [n]
    
lista = rangoHasta(5)
print(lista)