import heapq

def a_star(laberinto, inicio, final):
    """
    Encuentra el camino más corto en un laberinto utilizando A*.

    Args:
        laberinto: Una lista de listas representando el laberinto.
        inicio: La posición inicial como una tupla (fila, columna).
        final: La posición final como una tupla (fila, columna).

    Returns:
        Una lista de posiciones que representan el camino más corto.
    """

    filas, columnas = len(laberinto), len(laberinto[0])
    visitados = set()
    padre = {}
    cola = [(0, 0, inicio)]  # (f(n), g(n), posición)

    while cola:
        _, _, nodo = heapq.heappop(cola)
        fila, col = nodo

        if nodo == final:
            camino = []
            while nodo in padre:
                camino.append(nodo)
                nodo = padre[nodo]
            camino.append(inicio)
            camino.reverse()
            return camino

        visitados.add(nodo)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = fila + dr, col + dc
            if 0 <= r < filas and 0 <= c < columnas and laberinto[r][c] == 0 and (r, c) not in visitados:
                g = 1  # Costo de moverse a un vecino
                h = abs(r - final[0]) + abs(c - final[1])  # Heurística de Manhattan
                f = g + h
                padre[(r, c)] = nodo
                heapq.heappush(cola, (f, g, (r, c)))

    return None

# Ejemplo de uso:
laberinto = [
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]
inicio = (0, 0)
final = (4, 4)

camino = a_star(laberinto, inicio, final)
print(camino)