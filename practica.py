containerPila = []

containerPila.append(23)

containerPila.append(100)
containerPila.append(25)

print("Actualizacion antes del pop")
for elem in containerPila: 
    print(elem)

    aux1.containerPila.pop()
    print(f'the last element to be showed{aux1}')

    print("Actualizacion despues del pop")
    for elem in containerPila: 
     print(elem)

aux2=containerPila[-1]
print("Actualizacion despues del [-1]")
print(f'the last element: {aux2}')
for elem in containerPila: 
     print(elem)
