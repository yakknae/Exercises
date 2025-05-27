from collections import deque

class Elemento:
    def __init__(self,elemento):
        self.elemento = elemento
class Pila:
    def __init__(self):
        self.cola = deque()
    def apilar(self, elemento):
        self.cola.append(elemento)
    def desapilar(self):
        self.cola.pop()
        print("elemento eliminado")
    def mostrar(self):
        print("elementos: ")
        for n in reversed(self.cola):
            print(n.elemento)

pila = Pila()
elemento1 = Elemento("1")
elemento2 = Elemento("2")
pila.apilar(elemento1)
pila.apilar(elemento2)
pila.mostrar()
pila.desapilar()
pila.mostrar()
