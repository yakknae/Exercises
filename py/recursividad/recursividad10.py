def sinDuplicadosConSemilla(lista, resultado):
    if not lista:
        return resultado
    primero=lista[0]
    if primero not in resultado:
        resultado.append(primero)
    return sinDuplicadosConSemilla(lista[1:],resultado)

    

lista = [6,5,1,6,3,-1]
resultado = []
respuesta = sinDuplicadosConSemilla(lista,resultado)
print(respuesta)