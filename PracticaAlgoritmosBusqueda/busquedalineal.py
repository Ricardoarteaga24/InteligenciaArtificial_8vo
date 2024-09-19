def busqueda_lineal(lista, valor):
  """
  Realiza una búsqueda lineal en una lista.

  Args:
    lista: La lista donde se realizará la búsqueda.
    valor: El valor a buscar.

  Returns:
    El índice del valor si se encuentra, -1 en caso contrario.
  """

  for i in range(len(lista)):
    if lista[i] == valor:
      return i
  return -1

# Ejemplo de uso:
mi_lista = [3, 7, 4, 9, 5, 2, 6, 1]
valor_a_buscar = 1

indice = busqueda_lineal(mi_lista, valor_a_buscar)

if indice != -1:
  print("El valor", valor_a_buscar, "se encuentra en el espacio", indice)
else:
  print("El valor", valor_a_buscar, "no se encontró en la lista")