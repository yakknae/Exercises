from collections import deque
import time

class Ticket:
    def __init__(self,nombre_Cliente,id):
        self.nombre_Cliente = nombre_Cliente
        self.id = id

    def __str__(self):
        return f"Ticket ID: {self.id}, Cliente: {self.nombre_Cliente}"

class Cola:
    def __init__(self):
        self.cola = deque()
    
    def agregar_ticket(self,ticket):
        self.cola.append(ticket)
        print(f"ticket {ticket.nombre_Cliente} agregado a la cola.")
    
    def eliminar_ticket(self):
        if self.esta_vacia():
            print("la cola esta vacia")
        else:
            ticket_elimino = self.cola.popleft()
            print(f"el ticket {ticket_elimino} fue eliminado")
            return ticket_elimino

    def esta_vacia(self):
        return len(self.cola) == 0

    def mostrar_lista(self):
        if self.esta_vacia():
            print("la cola esta vacia")
        else:
            print("tickets en la cola")
            for t in self.cola:
                print(f"{t}")
        
c = Cola()

t1 = Ticket("María", 101)
t2 = Ticket("Juan", 102)
t3 = Ticket("Lucía", 103)

c.agregar_ticket(t1)
c.agregar_ticket(t2)
c.agregar_ticket(t3)

c.mostrar_lista()

c.eliminar_ticket()
c.mostrar_lista()
    
