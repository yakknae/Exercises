def sumaHasta(n):
    if n == 0:
        return 0
    else:
        return n + sumaHasta(n-1)
    
resultado = sumaHasta(5)
print(resultado)