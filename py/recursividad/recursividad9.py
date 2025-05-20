def sinDuplicados(lista):
    if not lista:
        return []
    
    primero = lista[0]
    resto = [x for x in lista[1:] if x != primero]
    return [primero] + sinDuplicados(resto)
    



lista = [6,5,1,6,3,-1]
resultado = sinDuplicados(lista)
print(resultado)