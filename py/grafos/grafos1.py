grafo = {}

# -- 1.Agregar nodo
def agregar_nodo(grafo,nodo):
    if nodo not in grafo:
        grafo[nodo] = []
        print(f"Nodo: {nodo} fue agregado al grafo")

# -- 2.Agregar arista
def agregar_arista(grafo,n1,n2):
    if n1 in grafo and n2 in grafo:
        grafo[n1].append(n2)
        grafo[n2].append(n1)
        print(f"Ahora los nodos {n1} y {n2} estan conectados")
    else:
        print("uno de los nodos no existe")

# -- 3.Verificar si estan conectados 2 nodos
def estan_conectados(grafo,n1,n2):
    if(n1 in grafo and n2 in grafo and n2 in grafo[n1]):
        return True
    else:
        return False
    
# -- 4. Verificar si un nodo esta aislado
def es_aislado(grafo,nodo):
      if nodo in grafo and len(grafo[nodo])==0:
           print(f"El nodo: {nodo} es un nodo aislado")
      else:
           print(f"El nodo: {nodo} no es un nodo aislado")
    
# -- 5.Mostrar nodo
def mostrar_nodo(grafo,nodo):
    if nodo  in grafo:
        return True
    else:
        return False

# -- 6.Mostrar nodos
def lista_nodo(grafo):
    return list(grafo.keys())

# -- 7.Mostrar grafo
def mostar_grafo(grafo):
     if not grafo:
          print("El grafo esta vacio")
     for nodo,vecinos in grafo.items():
          print(f"  {nodo} → {vecinos}")

# -- 8.Grado de un nodo
def grado_nodo(grafo,nodo):
     if nodo in grafo:
          return len(grafo[nodo])
     else:
          return -1

# -- 9.Eliminar una arista
def eliminar_arista(grafo,n1,n2):
    if n1 in grafo and n2 in grafo:
        if n2 in grafo[n1]:
            grafo[n1].remove(n2)
        if n1 in grafo[n2]:
            grafo[n2].remove(n1)
        print(f"arista eliminada entre los nodos: {n1} y {n2}")
    else:
         print(f"No hay una arista entre los nodos: {n1} y {n2}")

# -- 10.Eliminar un nodo
def eliminar_nodo(grafo,nodo):
    if nodo not in grafo:
        return 
    
    for otroNodo in grafo.values():
        if nodo in otroNodo:
            otroNodo.remove(nodo)
            print(f"Nodo: {nodo} eliminado del nodo {otroNodo}")
        
    del grafo[nodo]
    print(f"Nodo: {nodo} eliminado")

# -- MENU
def menu():
    print("\n=== Menú de Grafo ===")
    print("1. Agregar nodo")
    print("2. Agregar arista")
    print("3. Verificar si estan conectados los nodos")
    print("4. Verificar si esta aislado un nodo")
    print("5. Buscar nodo")
    print("6. Mostrar todos los nodos")
    print("7. Mostrar grafo")
    print("8. Grado de un nodo")
    print("9. Eliminar arista")
    print("10. Eliminar nodo")
    print("11. Salir")

#-----------------------------------------------------------------------------
agregar_nodo(grafo,'A')
agregar_nodo(grafo,'B')
agregar_nodo(grafo,'C')

agregar_arista(grafo,'A','B')
agregar_arista(grafo,'A','C')

print(estan_conectados(grafo,'A','B'))
print(estan_conectados(grafo,'A','C'))
print(estan_conectados(grafo,'A','D'))

print(grafo)

print(mostrar_nodo(grafo,'C'))

eliminar_nodo(grafo,'C')

print(mostrar_nodo(grafo,'C'))

print(grafo)
#-----------------------------------------------------------------------------


if __name__ == "__main__":
    while True:
        menu()
        opcion = input("ingrese una opcion del 1 al 7 ('0' para salir): ")
        if opcion == '1':
                valor = input("Que nodo queres agregar: ")
                if valor:
                    agregar_nodo(grafo,valor)
                    print(f"Nodo: {valor} insertado")
                else:
                    print("no se pudo agregar el nodo")
        elif opcion == '2':
                n1 = input("Nodo 1: ")
                n2 = input("Nodo 2: ")
                if n1 and n2:
                    agregar_arista(grafo,n1,n2)
                    print(f"Arista: entre {n1} y {n2} insertada")
                else:
                    print("no se pudo agregar la arista")
        elif opcion == '3':
                print("Que nodos queres verificar si estan conectados?: ")
                valor = input("Nodo 1: ")
                valor2 = input("Nodo 2: ")
                resultado = estan_conectados(grafo,valor,valor2)
                print("Sí" if resultado else "No")
        elif opcion == '4':
             valor = input("Cual nodo queres verificar si esta aislado: ")
             es_aislado(grafo,valor)
        elif opcion == '5':
            valor = input("Cual nodo queres buscar: ")
            resultado = mostrar_nodo(grafo,valor)
            print(resultado)
        elif opcion == '6':
             resultado = lista_nodo(grafo)
             print(resultado)
        elif opcion == '7':
             mostar_grafo(grafo)
        elif opcion == '8':
             valor = input("De que nodo queres saber su grado: ")
             resultado = grado_nodo(grafo,valor)
             print(resultado)
        elif opcion == '9':
                n1 = input("Nodo 1: ")
                n2 = input("Nodo 2: ")
                eliminar_arista(grafo,n1,n2)
        elif opcion == '10':
                valor = input("Que nodo queres eliminar: ")
                eliminar_nodo(grafo,valor)
        elif opcion == '11':
                print("saliendo del programa...")
                break
        else:
            print("Opcion no valida")

    
# funciones a agregar


