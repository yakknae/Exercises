from collections import deque
import heapq

grafo = {
    'a': [('b', 1), ('f', 8),('d',5)],
    'b': [('a', 1), ('c', 100),('e',10)],
    'c': [('b', 100), ('d', 4),('f',3)],
    'd': [('e', 7), ('c', 4),('a',5)],
    'e': [('f', 2), ('d', 7),('b',10)],
    'f': [('a', 8), ('e', 2),('c',3)]
}

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



# -- 9.BFS
def BFS(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    cola = deque([(inicio, [inicio])])
    visitados = set([inicio])

    while cola:
        nodo, camino = cola.popleft()
        print(f"Visitando al nodo: {nodo}")

        for vecino in grafo[nodo]:
            if vecino == objetivo:
                print("¡Objetivo encontrado!")
                return camino + [vecino]

            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_camino = camino + [vecino]
                cola.append((vecino, nuevo_camino))

    print("No encontrado")
    return None

# -- 10.DFS
def DFS(grafo,nodo,objetivo,visitados=None,camino=None):
     if visitados is None:
          visitados = set()
     if camino is None:
          camino = []
     

     print(f"Visitando al nodo: {nodo}") 
     camino.append(nodo)
     if nodo == objetivo:
        print("encontrado")
        return True
     visitados.add(nodo)

     for vecino in grafo[nodo]:
          if vecino not in visitados:
               if DFS(grafo,vecino,objetivo,visitados):
                    return True
     camino.pop()
     return False
    
#-- 11.Todos los caminos
def todos_los_caminos(grafo,inicio,fin,camino=None,costo_total=0):
     if camino is None: 
          camino = []
          

     camino = camino + [inicio]

     if inicio == fin:
          return[(camino,costo_total)]
     
     caminos=[]

     for vecino,peso in grafo[inicio]:
          if vecino not in camino:
               nuevo_camino = todos_los_caminos(grafo,vecino,fin,camino,costo_total+peso)
               caminos.extend(nuevo_camino)
     return caminos

# -- 12.Eliminar una arista
def eliminar_arista(grafo,n1,n2):
    if n1 in grafo and n2 in grafo:
        if n2 in grafo[n1]:
            grafo[n1].remove(n2)
        if n1 in grafo[n2]:
            grafo[n2].remove(n1)
        print(f"arista eliminada entre los nodos: {n1} y {n2}")
    else:
         print(f"No hay una arista entre los nodos: {n1} y {n2}")

# -- 13.Eliminar un nodo
def eliminar_nodo(grafo,nodo):
    if nodo not in grafo:
        return 
    
    for otroNodo in grafo.values():
        if nodo in otroNodo:
            otroNodo.remove(nodo)
            print(f"Nodo: {nodo} eliminado del nodo {otroNodo}")
        
    del grafo[nodo]
    print(f"Nodo: {nodo} eliminado")

# -- 14. Dijkstra
def dijkstra(grafo,inicio):
     distancias = {nodo:float('inf') for nodo in grafo}
     distancias[inicio] = 0

     cola = [(0,inicio)]

     while cola:
          distancia_actual, nodo_actual = heapq.heappop(cola)

          if distancia_actual > distancias[nodo_actual]:
               continue
          
          for vecino, peso in grafo[nodo_actual]:
               nueva_distancia = distancia_actual + peso

               if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola,(nueva_distancia,vecino))
                    
     return distancias

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
    print("9. BFS")
    print("10. DFS")
    print("11. Todos los caminos")
    print("12. Eliminar arista")
    print("13. Eliminar nodo")
    print("14. Dijkstra")
    print("15. Salir")

#-----------------------------------------------------------------------------
#agregar_nodo(grafo,'A')
#agregar_nodo(grafo,'B')
#agregar_nodo(grafo,'C')
#agregar_nodo(grafo,'D')
#agregar_nodo(grafo,'E')
#agregar_nodo(grafo,'F')

#agregar_arista(grafo,'A','B')
#agregar_arista(grafo,'A','F')
#agregar_arista(grafo,'A','D')
#agregar_arista(grafo,'B','C')
#agregar_arista(grafo,'C','D')
#agregar_arista(grafo,'D','E')
#agregar_arista(grafo,'E','F')
#agregar_arista(grafo,'B','E')
#agregar_arista(grafo,'C','F')


print(estan_conectados(grafo,'A','B'))
print(estan_conectados(grafo,'A','D'))
print(estan_conectados(grafo,'C','B'))
print(estan_conectados(grafo,'D','C'))


print(grafo)

print(mostrar_nodo(grafo,'C'))

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
                inicio = input("Inicio 1: ")
                objetivo = input("Objetivo 2: ")
                resultado = BFS(grafo,inicio,objetivo)
                print(resultado)
        elif opcion == '10':
                nodo = input("Nodo : ")
                objetivo = input("Objetivo: ")
                camino = DFS(grafo,nodo,objetivo)
                print(f"Camino encontrado: {camino}")
        elif opcion == '11':
                inicio = input("Nodo inicio: ")
                fin = input("Nodo final: ")
                caminos = todos_los_caminos(grafo,inicio,fin)
                #Camino mas barato
                camino_mas_barato=caminos[0][0]
                menor_costo=caminos[0][1]

                for camino,precio in caminos:
                    print(f"Camino: {camino} - Precio total: {precio}")

                for camino,precio in caminos:
                    if precio < menor_costo:
                         menor_costo=precio
                         camino_mas_barato=camino

                print(f"El camino más barato es: {camino_mas_barato} con un valor de {menor_costo}")

        elif opcion == '12':
                n1 = input("Nodo 1: ")
                n2 = input("Nodo 2: ")
                eliminar_arista(grafo,n1,n2)
        elif opcion == '13':
                valor = input("Que nodo queres eliminar: ")
                eliminar_nodo(grafo,valor)
        elif opcion == '14':
                inicio = input("Elije el nodo de inicio: ")
                distancias = dijkstra(grafo,inicio)
                print("Distancias más cortas desde", inicio)
                for nodo, distancia in distancias.items():
                    print(f"{inicio} -> {nodo}: {distancia}")
                     
        elif opcion == '15':
                print("saliendo del programa...")
                break
        else:
            print("Opcion no valida")

    
