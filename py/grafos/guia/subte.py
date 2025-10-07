import heapq

grafo = {
     #trenes
     'a': [('b',40),('c',30),('a1',10)],
     'b': [('d',30),('a',40),('b1',10)],
     'c': [('d',60),('a',30),('c1',10)],
     'd': [('b',30),('c',60),('d1',2)],
     #subtes
     'a1': [('a',10),('b1',38),('c1',30)],
     'b1': [('b',10),('d1',20),('a1',38)],
     'c1': [('c',10),('a1',30),('d1',25)],
     'd1': [('d',2),('c1',25),('b1',20)],

}

grafo2 = {
    # Trenes (nodos grandes)
    'A': [('B', 40), ('C', 30), ('A1', 10)],
    'B': [('D', 30)],
    'C': [('D', 60), ('C1', 10)],
    'D': [],

    # Subtes (nodos pequeños)
    'A1': [('B1', 38)],
    'B1': [('B', 10), ('D1', 20)],
    'C1': [('A1', 30), ('D1', 25)],
    'D1': [('D', 2)]
}

grafo3 = {
     #trenes
     'a': [('b',40),('c',30),('a1',10)],
     'b': [('d',30),('a',40),('b1',10)],
     'c': [('d',-24),('a',30),('c1',10)],
     'd': [('b',30),('c',-24),('d1',2)],
     #subtes
     'a1': [('a',10),('b1',38),('c1',30)],
     'b1': [('b',10),('d1',20),('a1',38)],
     'c1': [('c',10),('a1',30),('d1',-10)],
     'd1': [('d',2),('c1',-10),('b1',20)],

}


# -- Mostrar grafo
def mostar_grafo(grafo):
     if not grafo:
          print("El grafo esta vacio")
     for nodo,vecinos in grafo.items():
          print(f"  {nodo} → {vecinos}")
          
# --  Dijkstra
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

# -- bellman ford
def bellman_ford(grafo, origen):
    # Inicializar distancias
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0

    # Relajar aristas |V|-1 veces
    for _ in range(len(grafo) - 1):
        for u in grafo:
            for v, peso in grafo[u]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso

    # Detectar ciclos negativos
    for u in grafo:
        for v, peso in grafo[u]:
            if dist[u] + peso < dist[v]:
                print("⚠️ Hay un ciclo de peso negativo en el grafo.")
                return None

    return dist

#-- Todos los caminos
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


if __name__ == "__main__":
    while(True):
        opcion = input("elige una opcion: ")
        if opcion == '1':
         resultado = mostar_grafo(grafo3)
         print(resultado)
        elif opcion == '2':
            inicio = input("Elije el nodo de inicio: ")
            distancias = dijkstra(grafo2,inicio)
            print("Distancias más cortas desde", inicio)
            for nodo, distancia in distancias.items():
                print(f"{inicio} -> {nodo}: {distancia}")

        elif opcion == '3':
                inicio = input("Nodo inicio: ")
                fin = input("Nodo final: ")
                caminos = todos_los_caminos(grafo2,inicio,fin)
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

        elif opcion == '4':    
            print(bellman_ford(grafo3, 'a'))
