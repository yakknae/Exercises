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