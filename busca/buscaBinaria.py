#Busca Binária

def busca_binaria(valor, lista):
    inicio = 0
    fim = len(lista) - 1 
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if valor == lista[meio]:
            return meio
        elif valor < lista[meio]:
            fim = meio - 1 
        else:
            inicio = meio + 1
    return None

#PRINCIPAL
lista = [1,2,3,4,5,6,7]
print(f'Item: {busca_binaria(5,lista)}')