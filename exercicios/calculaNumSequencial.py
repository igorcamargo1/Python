"""Fazer uma função que tem como parâmetro de entrada um número inteiro positivo n e fornece como saída a soma de todos os números inteiros menores ou iguais a n."""

print("Calcula sequência de números até o 0.")
print("=====================================")

#=============================================================
def entradaDados():
    n = int(input("Digite o número que deseja somar até o 0:"))
    return n
#==============================================================
def controlador(n):
    cont = n 
    soma = 0
    while cont != 0:
        soma = soma + cont
        cont = cont - 1
    return soma
#===============================================================
def imprimir(result):
    print(f"o valor da soma foi de {result}")
#===============================================================
#Programa Principal

entrada = entradaDados()
processo  = controlador(entrada)
imprimir(processo)
