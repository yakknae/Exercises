from collections import deque

class Cliente:
    def __init__(self,nombre,cant):
        self.nombre = nombre
        self.cant = cant
    
    def __str__(self):
       return f"el nombre del cliente es {self.nombre} y la cantidad de articulos que lleva es {self.cant}"

class Supermercado:
    def __init__(self):
        self.cola = deque()
        
    
    def agregar_Cliente(self,cliente):
        self.cola.append(cliente)
    
    def eliminar(self):
        if self.esta_vacia():
            print("la cola esta vacia")
        else:
           cliente_eliminado = self.cola.popleft()
           print(f"el cliente eliminado fue {cliente_eliminado}")
        
    def mostrar_cola(self):
        print("los clientes de la cola son: ")
        for t in self.cola:
            print(f"{t}")

    

    def esta_vacia(self):
        return len(self.cola)==0
    
s = Supermercado()

cliente1 = Cliente("nico",5)
cliente2 = Cliente("eduardo",51)
cliente3 = Cliente("valen",27)

s.agregar_Cliente(cliente1)
s.agregar_Cliente(cliente2)
s.agregar_Cliente(cliente3)

s.mostrar_cola()

s.eliminar()

s.mostrar_cola()