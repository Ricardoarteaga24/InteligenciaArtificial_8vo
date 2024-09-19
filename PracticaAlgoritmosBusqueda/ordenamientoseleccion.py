def seleccion(lista):
  """
  Ordena una lista utilizando el algoritmo de selección.

  Args:
    lista: La lista a ordenar.
  """

  for i in range(len(lista) - 1):
    min_idx = i
    for j in range(i+1, len(lista)):
      if lista[min_idx] > lista[j]:
        min_idx = j
    # Swap the found minimum element with the first element
    lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Ejemplo de uso:
mi_lista = [64, 34, 25, 12, 22, 11, 90]
seleccion(mi_lista)
print("Lista ordenada:", mi_lista)