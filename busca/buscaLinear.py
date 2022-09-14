#Busca Linear

def busca_linear(valor, lista):
    for item in lista:
        if item == valor:
            return item #retorna o item encontrado   
    return None
#-------------------------------------------------------
def busca_linear2(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None
#-------------------------------------------------------
def busca_linear3(valor, lista):
    for i, item in enumerate(lista):
        if item == valor:
            return i #retorna o item encontrado 
    return None
#-------------------------------------------------------
#TO DO:
'''
1) Criar função (busca_linear), porém, retornando -1 como resposta para o valor encontrado. A ideia é manter a coerência do tipo do valor retornado em todos os casos, imprencindível em diversas linguagens

2) Crie uma função (busca_linear), porém, que o valor do retorno seja uma lista com os índices de todos os itens iguais ao valor buscado
'''

#programa principal 

lista = [3, 6, 5, 8, 0, 8, 2]
print(f'Item: {busca_linear(18,lista)}')
print(f'Indice: {busca_linear2(8,lista)}')
print(f'index: {busca_linear3(0, lista)}')