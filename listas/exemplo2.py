#atividade - manipulação de listas com funções
'''
1) Criar função tamanho_lista()
2) Criar função criar_lista()
3) Criar função imprimir_lista()
4) Criar função imprimir_pares()
5) Criar função imprimir_impares()
6) Criar função adicione os elementos impares em uma lista()
7) Criar função adicione os elementos pares em uma lista()
8) Crias função de busca de um elemento em uma lista()
'''
#--------------------------------------------------
def tamanho_lista():
    print('-- Tamanho da Lista --')
    t = int(input("Qual é o tamanho da lista:  "))
    return t
#--------------------------------------------------
def criar_lista(t):
    lista = list(range(t))
    print('-- Criando lista... --')
    print("----------------------")
    i = 0
    while i < t:
        lista[i] = int(input('Número:'))
        i += 1
    return lista
#--------------------------------------------------
def imprimir_lista(lista):
    print('-- Imprimindo os elementos da lista: --')
    for i in lista:
        print(f'Elemento: {i}')
#--------------------------------------------------
# Programa Principal
t = tamanho_lista()
lista = criar_lista(t)
imprimir = imprimir_lista(lista)


