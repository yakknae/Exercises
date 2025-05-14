def removerTodos(lista,elemento):
    if not lista:
        return []
    
    if lista[0] == elemento:
        return removerTodos(lista[1:], elemento)
    
    
    return [lista[0]] + removerTodos(lista[1:], elemento)
    

lista = [1,2,3,1,6,7,1,9,1]
elemento = 1

resultado =  removerTodos(lista,elemento)
print(resultado)