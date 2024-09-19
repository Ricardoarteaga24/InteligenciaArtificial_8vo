def burbuja(lista):
  """
  Ordena una lista utilizando el algoritmo de burbuja.

  Args:
    lista: La lista a ordenar.
  """

  n = len(lista)

  # Traverse through all array elements
  for i in range(n):
    swapped = False

    # Last i elements are already in place
    for j in range(0, n-i-1):

      # Traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if lista[j] > lista[j+1] :
        lista[j], lista[j+1] = lista[j+1], lista[j]
        swapped = True

    # IF no two elements were swapped by inner loop, then break
    if swapped == False:
      break

# Ejemplo de uso:
mi_lista = [64, 34, 25, 12, 22, 11, 90]
burbuja(mi_lista)
print("Lista ordenada:", mi_lista)