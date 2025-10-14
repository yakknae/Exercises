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
    'a': [('b', 40), ('c', 30), ('a1', 10)],
    'b': [('d', 30)],
    'c': [('d', 60), ('c1', 10)],
    'd': [],

    # Subtes (nodos pequeños)
    'a1': [('b1', 38)],
    'b1': [('b', 10), ('d1', 20)],
    'c1': [('a1', 30), ('d1', 25)],
    'd1': [('d', 2)]
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

grafo4 = {
    '1': [('4', 3), ('3', 2), ('2', 3)],
    '2': [('3', 1), ('5', 5),('1',3)],
    '3': [('1', 2), ('2', 1), ('4', 2), ('6', 8), ('5', 7)],
    '4': [('1', 3), ('3', 2), ('6', 6)],
    '5': [('2', 5), ('3', 7), ('6', 4)],
    '6': [('4', 6), ('3', 8), ('5', 4)]
}

def prim(grafo, inicio):
    visitados = set()
    mst = []
    peso_total = 0

    # Cola de prioridad: (peso, nodo_origen, nodo_destino)
    aristas = []
    visitados.add(inicio)

    for vecino, peso in grafo[inicio]:
        heapq.heappush(aristas, (peso, inicio, vecino))

    while aristas and len(visitados) < len(grafo):
        peso, u, v = heapq.heappop(aristas)

        if v not in visitados:
            visitados.add(v)
            mst.append((u, v, peso))
            peso_total += peso

            for vecino, peso2 in grafo[v]:
                if vecino not in visitados:
                    heapq.heappush(aristas, (peso2, v, vecino))

    return mst, peso_total


# Implementación de Kruskal con Union-Find
# Estructura Union-Find
class UnionFind:
    def __init__(self, vertices):
        self.padre = {v: v for v in vertices}
        self.rango = {v: 0 for v in vertices}

    def find(self, v):
        if self.padre[v] != v:
            self.padre[v] = self.find(self.padre[v])  # compresión de caminos
        return self.padre[v]

    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)

        if raiz_u != raiz_v:
            if self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            elif self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1
            return True
        return False


def kruskal(grafo):
    # Crear lista de aristas
    aristas = []
    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            aristas.append((peso, nodo, vecino))

    # Ordenar aristas por peso
    aristas.sort()

    # Inicializar Union-Find
    uf = UnionFind(grafo.keys())

    mst = []  # guardar aristas del árbol de expansión mínima
    peso_total = 0

    for peso, u, v in aristas:
        if uf.union(u, v):
            mst.append((u, v, peso))
            peso_total += peso

    return mst, peso_total


# -- menu
def menu():
     print("""
     1. Mostrar grafo
     2. Dijkstra
     3. Todos los caminos
     4. Bellman Ford
     5. DFS sin aristas negativas
     6. Kruskal
     7. Prim
     """)

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

# -- DFS sin aristas negativas
def dfs_sin_aristas_negativas(grafo, origen, visitados=None, camino_actual=None, todos_caminos=None):
    if visitados is None:
        visitados = set()
    if camino_actual is None:
        camino_actual = [origen]
    if todos_caminos is None:
        todos_caminos = []

    visitados.add(origen)
    todos_caminos.append(camino_actual.copy())

    for vecino, peso in grafo.get(origen, []):
        if peso < 0:
            # 🚫 Camino no válido: no seguimos por esta arista
            print(f"⚠️  Camino {' -> '.join(camino_actual)} -> {vecino} descartado (peso negativo: {peso})")
            continue  # ¡simplemente saltamos esta arista!

        if vecino not in visitados:
            dfs_sin_aristas_negativas(
                grafo, vecino, visitados.copy(), camino_actual + [vecino], todos_caminos
            )

    return todos_caminos

if __name__ == "__main__":
    while(True):
        menu()
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
                caminos = todos_los_caminos(grafo3,inicio,fin)
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

        elif opcion == '5':
            inicio = input("Nodo inicio: ")
            todos_caminos = dfs_sin_aristas_negativas(grafo3, inicio)
            print(f"Todos los caminos desde {inicio} sin aristas negativas:")
            for camino in todos_caminos:
                print(" -> ".join(camino))
        
        elif opcion == '6':
            mst, total = kruskal(grafo4)
            print("Árbol de recubrimiento mínimo:", mst)
            print("Peso total:", total)

        elif opcion == '7':
            mst, total = prim(grafo4, '1')
            print("Árbol de recubrimiento mínimo (Prim):", mst)
            print("Peso total:", total)
