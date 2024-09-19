def merge_sort(lista):
  """
  Ordena una lista utilizando el algoritmo de Merge Sort.

  Args:
    lista: La lista a ordenar.
  """

  if len(lista) > 1:
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Llamadas recursivas para ordenar las sublistas
    merge_sort(izquierda)
    merge_sort(derecha)

    # Combinar las sublistas ordenadas
    i = j = k = 0
    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] <= derecha[j]:
        lista[k] = izquierda[i]
        i += 1
      else:
        lista[k] = derecha[j]
        j += 1
      k += 1

    # Copiar los elementos restantes (si los hay)
    while i < len(izquierda):
      lista[k] = izquierda[i]
      i += 1
      k += 1

    while j < len(derecha):
      lista[k] = derecha[j]
      j += 1
      k += 1

# Ejemplo de uso:
mi_lista = [64, 94, 25, 45, 22, 11, 90]
merge_sort(mi_lista)
print("Lista ordenada:", mi_lista)