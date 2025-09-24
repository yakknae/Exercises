import math
from itertools import permutations

coordenadas = {
    'a': (1, 1),
    'b': (30, 40),
    'c': (80, 60),
    'd': (120, 30),
    'e': (150, 100),
    'f': (20, 30),
    'g':(100,80) }

#grafo = {
#    'a': ['b', 'c'],
#    'b': ['a', 'd','f'],
#    'c': ['a', 'd'],
#    'd': ['b', 'c', 'e'],
#    'e': ['d', 'f'],
#    'f': ['e','b']
#}
def crear_grafo(coordenadas):
    grafo = {}
    for nodo1 in coordenadas:
        grafo[nodo1] = []
        for nodo2 in coordenadas:
            if nodo1 != nodo2:
                grafo[nodo1].append(nodo2)
    return grafo

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
    total += distancia_entre_nodos(camino[-1], camino[0], coordenadas)
    return(total)

def vecino_cercano(grafo,coordenadas,inicio):
    visitados = set()
    actual = inicio
    camino = [inicio]
    visitados.add(actual)
    total_distancia = 0.0

    while len(visitados) < len(coordenadas):
        vecinos = grafo[actual]
        vecinos_no_visitados = []

        for vecino in vecinos:
            if vecino not in visitados:
                vecinos_no_visitados.append(vecino)

        if len(vecinos_no_visitados) == 0:
            break

        siguiente = vecinos_no_visitados[0]
        menor_distancia = distancia_entre_nodos(actual,siguiente,coordenadas)
        
        for vecino in vecinos_no_visitados:
            d = distancia_entre_nodos(actual,vecino,coordenadas)
            if d < menor_distancia:
                menor_distancia = d
                siguiente = vecino

        total_distancia += menor_distancia
        camino.append(siguiente)
        visitados.add(siguiente)
        actual = siguiente

    distancia_de_regreso = distancia_entre_nodos(actual, inicio, coordenadas)
    total_distancia += distancia_de_regreso
    camino.append(inicio)

    return camino,total_distancia


    

if __name__ == "__main__":
    print("------------- G R A F O -----------------")
    grafo = crear_grafo(coordenadas)
    resultado = mostrar_grafo(grafo)
    print(resultado)
    print("-------------------------------------")
    all_nodos = set(coordenadas.keys())
    caminos_completos =todos_caminos(grafo,'a',all_nodos)

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
    print("-------------------------------------")
    print("------------- Vecino más cercano -----------------")
    camino,distancia = vecino_cercano(grafo,coordenadas,'a')
    print("Camino encontrado:", camino)
    print("Distancia total:", distancia)
