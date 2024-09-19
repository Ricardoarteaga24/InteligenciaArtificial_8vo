def quicksort(lista, izquierda, derecha):
  """
  Ordena una lista utilizando el algoritmo quicksort.

  Args:
    lista: La lista a ordenar.
    izquierda: Índice del primer elemento.
    derecha: Índice del último elemento.
  """

  if izquierda < derecha:
    pivote = particionar(lista, izquierda, derecha)
    quicksort(lista, izquierda, pivote - 1)
    quicksort(lista, pivote + 1, derecha)

def particionar(lista, izquierda, derecha):
  """
  Particiona una lista en torno a un pivote.

  Args:
    lista: La lista a particionar.
    izquierda: Índice del primer elemento.
    derecha: Índice del último elemento.

  Returns:
    El índice del pivote.
  """

  pivote = lista[derecha]
  i = izquierda - 1

  for j in range(izquierda, derecha):
    if lista[j] < pivote:
      i += 1
      lista[i], lista[j] = lista[j], lista[i]

  lista[derecha], lista[i + 1] = lista[i + 1], lista[derecha]
  return i + 1

# Ejemplo de uso:
mi_lista = [64, 34, 25, 12, 85, 11, 90]
quicksort(mi_lista, 0, len(mi_lista) - 1)
print("Lista ordenada:", mi_lista)