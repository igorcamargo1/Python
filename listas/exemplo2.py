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
    print("=============================================")
    print("")
    print('-- Criando lista... --')
    print("----------------------")
    i = 0
    while i < t:
        lista[i] = int(input('Número:'))
        i += 1
    return lista
#--------------------------------------------------
def imprimir_lista(lista):
    print("=============================================")
    print("")
    print('-- Imprimindo os elementos da lista: --')
    for i in lista:
        print(f'Elemento: {i}')
    return i 
#--------------------------------------------------
def imprimir_pares(lista):
    print("=============================================")
    print("")
    for i in lista:
        if i % 2 == 0:
            print(f"Elementos pares: {i}")
#--------------------------------------------------
def imprimir_impares(lista):
    print("=============================================")
    print("")
    for i in lista:
        if i % 2 == 1:
            print(f"Elementos impares: {i}")
    return i
#--------------------------------------------------
def add_impares(lista):
    print("=============================================")
    print("")
    impar = int(input("Qual número você quer adicionar?"))
    if impar % 2 == 1:
        lista.append(impar)
        print("elemento adicionado a lista com sucesso!")
        print(f"lista: {lista}")
    else:
        print("Elemento não é impar, não foi adiconado a lista.")
    return impar
#--------------------------------------------------
def add_pares(lista):
    print("=============================================")
    print("")
    par = int(input("Qual número você quer adicionar?"))
    if par % 2 == 0:
        lista.append(par)
        print("elemento adicionado a lista com sucesso!")
        print(f"lista: {lista}")
    else:
        print("Elemento não é par, não foi adiconado a lista.")
    return par
#--------------------------------------------------
def busca_elemento(lista):
    print("=============================================")
    print("")
    busca = int(input("Qual elemento você deseja buscar na lista?"))
    if busca in lista:
        print(f"O elemento {busca} está na lista!")
    else: 
        print(f"O elemento {busca} não está na lista.")
#--------------------------------------------------
def principal():
    stop = 1
    while stop == 1:
        tamanho = tamanho_lista()
        criar = criar_lista(tamanho)
        imprimir_pares(criar)
        imprimir_impares(criar)
        add_pares(criar)
        add_impares(criar)
        busca_elemento(criar)
        stop = int(input("Caso queira encerrar o programa, digite 0, se quer continuar, digite 1:  "))
#--------------------------------------------------

principal()

