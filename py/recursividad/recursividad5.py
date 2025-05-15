def aparear(lista1,lista2):
    if not lista1 or not lista2:
        return []

    return [(lista1[0], lista2[0])] + aparear(lista1[1:],lista2[1:])

lista1=[1,2,3]
lista2=["a","b","c"] 
resultado = aparear(lista1,lista2)
print(resultado)