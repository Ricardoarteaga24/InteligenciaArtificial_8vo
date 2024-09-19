from collections import deque

def bfs(grafo, inicio):
    """
    Realiza una búsqueda en anchura en un grafo.

    Args:
        grafo: Una lista de adyacencia que representa el grafo.
        inicio: El vértice inicial.
    """

    visitados = set()  # Conjunto para marcar vértices visitados
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo)
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                cola.append(vecino)

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(grafo, 'A')