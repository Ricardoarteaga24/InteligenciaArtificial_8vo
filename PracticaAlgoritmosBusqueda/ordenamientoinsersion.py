def insercion(lista):
  """
  Ordena una lista utilizando el algoritmo de inserción.

  Args:
    lista: La lista a ordenar.
  """

  for i in range(1, len(lista)):
    clave = lista[i]
    j = i-1
    while j >=0 and clave < lista[j] :
        lista[j+1] = lista[j]
        j -= 1
    lista[j+1] = clave

# Ejemplo de uso:
mi_lista = [64, 34, 25, 12, 22, 11, 90]
insercion(mi_lista)
print("Lista ordenada:", mi_lista)