numeros = [1, 2, 3, 1, 6, 7, 1, 9, 1]

def sinDuplicados(lista):
    if len(lista) == 0:
        return []
    else:
        if lista[0] in lista[1:]:
            return sinDuplicados(lista[1:])
        else:
            return [lista[0]] + sinDuplicados(lista[1:])
        
print("Lista original:", numeros)
numerosSinDuplicados = sinDuplicados(numeros)
print("Lista sin duplicados:", numerosSinDuplicados)