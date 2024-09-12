def busqueda_binaria(lista, valor):
  """
  Realiza una búsqueda binaria en una lista ordenada.

  Args:
    lista: La lista ordenada donde se realizará la búsqueda.
    valor: El valor a buscar.

  Returns:
    El índice del valor si se encuentra, -1 en caso contrario.
  """

  izquierda = 0
  derecha = len(lista) - 1

  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if lista[medio] == valor:
      return medio
    elif valor < lista[medio]:
      derecha = medio - 1
    else:
      izquierda = medio + 1

  return -1

# Ejemplo de uso:
mi_lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valor_a_buscar = 4

indice = busqueda_binaria(mi_lista_ordenada, valor_a_buscar)

if indice != -1:
  print("El valor", valor_a_buscar, "se encuentra en el índice", indice)
else:
  print("El valor", valor_a_buscar, "no se encontró en la lista")