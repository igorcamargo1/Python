'''1) Crie uma função que receba uma matriz numérica como argumento e retorne o valor

da soma de seus itens. Acesse os itens da matriz indexando-a com os dois índices.'''

def cria_matriz(nLinhas, nColunas):
    '''
    (int,int) --> matriz numérica
    '''
    matriz = [] 
    for i in range(nLinhas):
        linha=[]
        for j in range(nColunas):
            n =int(input('Item: '))
            linha.append(n)
            matriz.append(linha)
    return matriz

def somaItens(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma
#----------------------------------------

def principal():
    matriz = cria_matriz(3,3)
    soma= somaItens(matriz)
    print(f'Soma: {soma}')
#-----------------------------------------
#Programa Principal
principal()
