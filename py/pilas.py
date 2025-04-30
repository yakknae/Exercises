from collections import deque

print("--------------Ejercicio 1-------------------")

def lista_vacia(stack):
    return len(stack)==0

my_stack = deque([5,10,15])

print(f"Lista original {my_stack}")

eliminado = my_stack.pop()

print(f"numero eliminado: {eliminado}")

while not lista_vacia(my_stack):
         nro_eliminado = my_stack.pop()
         print(f"el numero eliminado fue: {nro_eliminado}")

if lista_vacia(my_stack):
     print("la lista esta vacia")

print("--------------Ejercicio 2-------------------")

def invertir_palabra(palabra):
      stack = deque()

      for letra in palabra:
            stack.append(letra)
      print(stack)

      palabra_invertida = ""

      while stack: 
            palabra_invertida += stack.pop()
      return palabra_invertida

palabra = input("Escriba una palabra: ")
palabra_invertida = invertir_palabra(palabra)
print(f"la palabra fue {palabra} y invertida queda {palabra_invertida}")

print("--------------Ejercicio 3-------------------")
class Tarea:
    def __init__(self,titulo,descripcion):
        self.titulo = titulo
        self.descripcion = descripcion

    def __str__(self):
        return f"el titulo de la tarea es {self.titulo} y la descripcion es {self.descripcion}"

class Pila:
    def  __init__(self):
        self.cola = deque()

    def agregar_Tarea(self,tarea):
        self.cola.append(tarea)
    
    def eliminar_Tarea(self):
        if self.vacia2():
            print("no hay tareas")
        else:
            tarea_eliminada = self.cola.pop()
            print(f"la tarea eliminada fue {tarea_eliminada}")
    
    def mostrar_Tareas(self):
        print("las tareas son")
        for f in self.cola:
            print(f"{f}")
    
    def vacia2(self):
        return len(self.cola)==0
    
pila = Pila()
tarea1 = Tarea("examen","lokura")
tarea2 = Tarea("examen11","tremendo")

pila.agregar_Tarea(tarea1)
pila.agregar_Tarea(tarea2)

pila.mostrar_Tareas()

pila.eliminar_Tarea()

pila.mostrar_Tareas()
