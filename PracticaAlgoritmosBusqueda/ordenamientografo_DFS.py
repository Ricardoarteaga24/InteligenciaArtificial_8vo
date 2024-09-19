def dfs(grafo, inicio, visitados=None):
    """
    Realiza una búsqueda en profundidad en un grafo.

    Args:
        grafo: Una lista de adyacencia que representa el grafo.
        inicio: El vértice inicial.
        visitados: Un conjunto para marcar vértices visitados.
    """

    if visitados is None:
        visitados = set()

    visitados.add(inicio)
    print(inicio)

    for vecino in grafo[inicio]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(grafo, 'F')