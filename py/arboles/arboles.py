from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def insertar(raiz, valor):
    nuevo_nodo = Nodo(valor)
    if raiz is None:
        return nuevo_nodo
    
    cola = deque([raiz])

    while cola:
        actual = cola.popleft()

        if actual.izq is None:
            actual.izq = nuevo_nodo
            return
        else:
            cola.append(actual.izq)

        if actual.der is None:
            actual.der = nuevo_nodo
            return
        else:
            cola.append(actual.der)

# Construcción del árbol
#raiz = Nodo('F')
#raiz.izq = Nodo('B')
#raiz.der = Nodo('G')
#raiz.izq.izq = Nodo('A')
#raiz.izq.der = Nodo('D')
#raiz.izq.der.izq = Nodo('C')
#raiz.izq.der.der = Nodo('E')
#raiz.der.der = Nodo('I')
#raiz.der.der.izq = Nodo('H')

#raiz = Nodo('O')
#raiz.izq = Nodo('A')
#raiz.der = Nodo('V')
#raiz.izq.der = Nodo('L')
#raiz.izq.der.izq = Nodo('E')
#raiz.izq.der.der = Nodo('N')
#raiz.izq.der.izq.der = Nodo('I')
#raiz.izq.der.izq.izq = Nodo('C')
#raiz.izq.der.der.der = Nodo('T')
#raiz.izq.der.der.der.der = Nodo('U')

raiz = Nodo('C')
raiz.izq = Nodo('E')
raiz.der = Nodo('O')
raiz.izq.der = Nodo('I')
raiz.izq.izq = Nodo('A')
raiz.der.der = Nodo('L')
raiz.der.izq = Nodo('V')
raiz.der.der.izq = Nodo('N')
raiz.der.der.der = Nodo('T')
raiz.der.der.der.der = Nodo('U')

# Insertar un nuevo nodo
insertar(raiz, 'Z')

def preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        preorden(nodo.izq)
        preorden(nodo.der)

def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        print(nodo.valor, end=' ')
        inorden(nodo.der)

def postorden(nodo):
    if nodo:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=' ')

def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izq), altura(nodo.der))

def balance(nodo):
    if nodo is None:
        return 0
    return altura(nodo.izq) - altura(nodo.der)


print("\n")
print("preorden: ")
print(preorden(raiz))
print("\n")
print("inorden: ")
print(inorden(raiz))
print("\n")
print("postorden: ")
print(postorden(raiz))
print("\n")
print("altura: ",altura(raiz))
print("\n")
print("balance: ",balance(raiz))
print("\n")

