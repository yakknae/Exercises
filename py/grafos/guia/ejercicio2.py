from collections import deque

grafo = {
    'a': ['b','c'],
    'b': ['d'],
    'c': [],
    'd': ['c'],

}

in_degree = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 1,

}

def mostar_grafo(grafo):
     if not grafo:
          print("El grafo esta vacio")
     for nodo,vecinos in grafo.items():
          print(f"  {nodo} → {vecinos}")


def kahn_casero(in_degree,grafo):
    orden = []
    cola = deque()

    for nodo,grado in in_degree.items():
        if grado == 0:
            cola.append(nodo)

    while cola:
        actual = cola.popleft()
        orden.append(actual)

        for vecino in grafo.get(actual, []):
            in_degree[vecino] -= 1
            if in_degree[vecino] == 0:
                print("degree descontando:",in_degree)
                cola.append(vecino)
    
    return orden 



def kahn_topologico(grafo):
    # Paso 1: Calcular in-degree (cuántas flechas entran a cada nodo)
    in_degree = {nodo: 0 for nodo in grafo}
    
    for nodo in grafo:
        for vecino in grafo[nodo]:
            in_degree[vecino] += 1
            print("degree",in_degree)
    # Paso 2: Cola con nodos que tienen in-degree 0
    cola = deque([nodo for nodo in in_degree if in_degree[nodo] == 0])
    orden = []

    while cola:
        actual = cola.popleft()
        orden.append(actual)

        # Para cada vecino, reducir in-degree
        for vecino in grafo.get(actual, []):
            in_degree[vecino] -= 1
            if in_degree[vecino] == 0:
                cola.append(vecino)

    # Verificar si hay ciclo (si no incluye todos los nodos)
    if len(orden) != len(grafo):
        return None  
    return orden





if __name__ == "__main__":
    resultado = mostar_grafo(grafo);
    print("Recorrido desde 'a' hasta 'd':",kahn_topologico(grafo))
    print("Recorrido desde 'a' hasta 'd':",kahn_casero(in_degree,grafo))