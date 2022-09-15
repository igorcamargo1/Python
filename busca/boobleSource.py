def troca(lista, i, j):
    lista[i], lista [j] = lista[j], lista[i]


#Programa Principal

lista = [40, 30, 20, 50, 10]

for i in range(len(lista) - 1):
    if lista[i] > lista[i+1]:
        troca(lista,i,i+1)
print(lista)