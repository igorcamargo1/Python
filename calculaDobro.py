'''1.Escreva  um  programa  que  leia  um  número  do  teclado,  calcule  o  dobro  do número
 lido e imprima o resultado. O programa deve ter:
 •Função para entrada de dados
 •Função para calcular o dobro do número
 •Função para imprimir o resultado
 •Programa Principal para testar as funções acima'''

print("Calcula dobro")
print("==============")

#===============================================
def entradaDados():
    n = int(input("Digite o número que você deseja dobrar:"))
    return n
#===============================================
def calculaDobro(n):
    dobro = n*2
    return dobro
#===============================================
def imprimir(result):
    print(f"o resultado foi {result}")
#===============================================
#programa principal

entrada = entradaDados()
processo = calculaDobro(entrada)
imprimir(processo)