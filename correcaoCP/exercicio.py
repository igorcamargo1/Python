''' 1.(10,0) Sistema de monitoramento de temperaturas.
 •Um  sistema  de  monitoramento  de  temperaturas  está  em  operação  em  uma  cidade  no sudeste brasileiro, porém, é preciso melhorá-lo e expandir o seu uso para outras cidades. Para  isto,  você  foi  contratado  para  desenvolver  um  novo  sistema  em  Python  que  faça  o mapeamento  das  temperaturas  médias  em  um  determinado  período  e  que  seja  capaz  de dar algumas informações sobre esses dados.
•Como  parte  dos  requisitos,  o  programa  deve  coletar  algumas  temperaturas  médias (diárias),  durante  um  período  determinado  pelo  usuário  (mapeados  em  dias/semana), permita a impressão de todas as temperaturas mapeadas, a maior e a menor temperatura lida,  a  média  das  temperaturas  mapeadas,  e  uma  lista  com  as  temperaturas  negativas. Para isso, escreva um programa que tenha:
•1) Uma função que solicite ao usuário qual o período será mapeado (dias/semana)
•2) Uma função para mapear/coletar as temperaturas em uma matriz (dias/semana)
•3) Uma  função para obter a maior e a menor temperatura mapeada no período
•4)  Uma  função  para  "separar"  (em  uma  lista)  as temperaturas  negativas  no  período mapeado
•5) Uma função para obter a temperatura média no período
•6) Função principal para testar o programaObs.: A implementação do programa utilizando apenas o conceito de listas será permitido, porém, com o devido ajuste da nota de cada item que especifica o uso de lista de listas. Entrega: A entrega deverá ser feita exclusivamente pelo portal do aluno. Não serão aceitas as entregas pelo Teams.

'''



'''
() -> lista
Descrição: Função que obtem a cardinalidade de uma matriz (linha e coluna)
Retorno: uma lista contendo o número de linhas e colunas obtidas pelo usuário
'''
def obter_n_cardinalidade():
    cardinalidade = []
    linha = int(input('Linhas: '))
    cardinalidade.append(linha)
    coluna = int(input('Colunas: '))
    cardinalidade.append(coluna)
    return cardinalidade

'''
(int,int) -> matriz
Recebe o número de linhas e colunas, cria a matriz, preenche e retorna uma matriz preenchida com as temperaturas médias no período definido pelo usuário
'''
def crias_matriz(cardinalidade):
    matriz =[]
    for i in range(cardinalidade[0]):
        linha = []
        for j in range(cardinalidade[1]):
            temp = int(input('Temperatura: '))
            linha.append(temp)
        matriz.append(linha)
    return matriz
#----------------------------------------------
def obter_soma_temperaturas(matriz):
    soma = 0
    for linha in matriz:
        for coluna in linha:
            soma += coluna
    return soma
#----------------------------------------------
def obter_maior_menor_temperatura(matriz):
    menor = matriz [0][0]
    maior = matriz [0][0]
    for linha in matriz:
        for coluna in linha:
            if coluna < menor:
                menor = coluna
            if coluna > maior:
                maior = coluna
    lista = [maior, menor]
    return lista
#----------------------------------------------
def obter_temperaturas_negativas(matriz):
    temp_negativas = []
    for linha in matriz:
        for coluna in linha:
            if coluna < 0:
                temp_negativas.append(coluna)
    return temp_negativas
#----------------------------------------------
def obter_media_temperaturaas(matriz):
    media= obter_soma_temperaturas(matriz) / (len(matriz) * len(matriz[0]))
    return media
#----------------------------------------------
def imprimir_dados(matriz, soma, m_m, media, temp_negativas):
    print('==============================================')
    print('================= Relatório ==================')
    print('==============================================')
    print(f'Matriz: {matriz}')
    print(f'Soma: {soma}')
    print(f'Menor: {m_m[0]} | Maior: {m_m[1]}')
    print(f'Média: {media:.2f}')
    print(f'Temperaturas negativas: {temp_negativas}')
#----------------------------------------------
def principal():
    cardinalidade = obter_n_cardinalidade()
    matriz = crias_matriz(cardinalidade)
    soma = obter_soma_temperaturas(matriz)
    m_m = obter_maior_menor_temperatura(matriz)
    media = obter_media_temperaturaas(matriz)
    temp_negativas = obter_temperaturas_negativas(matriz)
    imprimir_dados(matriz, soma, m_m, media, temp_negativas)
#----------------------------------------------
principal()