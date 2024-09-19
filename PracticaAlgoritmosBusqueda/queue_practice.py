containerFila=[]

containerFila.append(12)
containerFila.append(19)
containerFila.append(50)

for i in containerFila:
    print(i)

print("after pop")

containerFila.pop(0)
for i in containerFila:
    print(i)