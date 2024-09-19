import heapq

def dijkstra(grafo, inicio):
    """
    Encuentra los caminos más cortos desde un vértice inicial a todos los demás vértices en un grafo.

    Args:
        grafo: Una lista de adyacencia que representa el grafo.
        inicio: El vértice inicial.

    Returns:
        Un diccionario que contiene las distancias más cortas desde el vértice inicial a todos los demás vértices.
    """

    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        distancia, nodo = heapq.heappop(cola)

        if distancia > distancias[nodo]:
            continue

        for vecino, peso in grafo[nodo].items():
            nueva_distancia = distancia + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))

    return distancias

# Ejemplo de uso:
grafo = {
    'A': {'B': 4, 'C': 3},
    'B': {'D': 2, 'E': 3},
    'C': {'F': 5},
    'D': {'E': 1},
    'E': {'F': 4},
    'F': {}
}

distancias_minimas = dijkstra(grafo, 'A')
print(distancias_minimas)