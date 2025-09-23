import math
from itertools import permutations

coordenadas = {
    'a': (2, 1),
    'b': (1, 2),
    'c': (1, 3),
    'd': (2, 4),
    'e': (3, 3),
    'f': (3, 2)
}

grafo = {
    'a': ['b', 'c'],
    'b': ['a', 'd','f'],
    'c': ['a', 'd'],
    'd': ['b', 'c', 'e'],
    'e': ['d', 'f'],
    'f': ['e','b']
}


def todos_caminos(grafo, inicio,todos_nodos, camino=None):
    if camino is None:
        camino = []

    camino = camino + [inicio] 

    if set(camino) == todos_nodos:
        return [camino] 

    caminos = []

    for vecino in grafo[inicio]:
        if vecino not in camino:  
            nuevos_caminos = todos_caminos(grafo, vecino,todos_nodos, camino)
            caminos.extend(nuevos_caminos)

    return caminos

def mostrar_grafo(grafo):
    if not grafo:
        print("El grafo esta vacio")
    for nodo,vecino in grafo.items():
        print(f"{nodo} -> {vecino}")
    

def distancia_entre_nodos(nodo1,nodo2,coordenadas):
    x1,y1 = coordenadas[nodo1]
    x2,y2 = coordenadas[nodo2]
    return math.sqrt((x2-x1)**2+ (y2-y1)**2)

def distancia_camino(camino,coordenadas):
    if len(camino) < 2:
        return 0.0
    
    total = 0.0
    for i in range(len(camino)-1):
        total += distancia_entre_nodos(camino[i],camino[i+1],coordenadas)
    return(total)
    

if __name__ == "__main__":
    print("------------- G R A F O -----------------")
    resultado = mostrar_grafo(grafo)
    print(resultado)
    print("-------------------------------------")
    all_nodos = set(coordenadas.keys())
    caminos_completos =todos_caminos(grafo,'e',all_nodos)

    mejor_camino = None
    mejor_distancia = None
    print("------------- TODOS LOS CAMINOS -----------------")
    for camino in caminos_completos:
        d = distancia_camino(camino,coordenadas)
        print(f"Camino: {camino} → Distancia: {d:.2f}")
       

        if mejor_distancia == None or d < mejor_distancia:
            mejor_distancia = d
            mejor_camino = camino
    print("-------------------------------------")
    print(f"\n Camino más corto encontrado:")
    print(f"\ncamino: {mejor_camino}")
    print(f"\ndistancia: {mejor_distancia}")


