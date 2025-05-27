from collections import deque
class Elemento:
    def __init__(self,elemento):
        self.elemento = elemento
    def __str__(self):
        return str(self.elemento)  # Define cómo se imprime el objeto.
class Cola:
    def __init__(self):
        self.cola = deque()
    def apilar(self, elemento):
        self.cola.append(elemento)
    def desapilar(self):
        if self.vacia():
            print("la cola esta vacia")
        else:
            eliminado = self.cola.popleft()
            print(f"el elemento {eliminado} fue eliminado")
            return eliminado
    def mostrar(self):
        if self.vacia():
            print("la cola esta vacia")
        else:
            print("la cola actual cuenta con los elementos: ")
            for n in self.cola:
                print(n)

    def vacia(self):
        return len(self.cola)==0
    
c = Cola()
Elemento1 = Elemento(5)
Elemento2 = Elemento(10)
Elemento3 = Elemento(15)

c.apilar(Elemento1)
c.apilar(Elemento2)
c.apilar(Elemento3)

c.mostrar()
c.desapilar()
c.mostrar()