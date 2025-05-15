

###################################
def sumarN(n,numeros):
    if n == 0 or not numeros:
        return 0
    
    return numeros[0] + sumarN(n-1,numeros[1:])

numero = 5
numeros = [2, 4, 6, 8, 10, 12]

resultado = sumarN(numero,numeros)
print(resultado)