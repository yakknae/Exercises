def ordenar(lista):
    if len(lista) <=1:
        return lista
    
    minimo = 0
    for i in range(1, len(lista)):
        if lista[i] <= lista[minimo]:
            minimo = i
    
    primero = lista[minimo]
    resto = lista[:minimo] + lista[minimo + 1:]
    return [primero] + ordenar(resto)



lista = [6,3,-1]
resultado = ordenar(lista)
print(resultado)