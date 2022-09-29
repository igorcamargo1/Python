



def merge_sort(lista):
    if len(lista) > 1:

        #encontrando o meio da lista
        meio = len(lista) // 2

        #dividindo a lista em duas L e R
        left = lista[:meio]
        right = lista[meio:]

        #ordenando a primeira lista
        merge_sort(left)

        #ordenando a segunda lista
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lista[j] = left[i]
                i+=1
            else:
                lista[k] = right[j]
                j+=1
            k+=1


        #verificando os elementos da lista left
        while i < len(left):
            lista[k] = left[i]
            i+=1
            k+=1

        #verificando os elementos da lista right
        while j < len(right):
            lista[k] = right[j]
            j+=1
            k+=1
#-------------------------------------------------------------------------

lista = [12, 11, 13 , 5, 6, 7] 
print(f'Lista:{lista}')
merge_sort(lista)
print(f'Lista ordenada: {lista}')
