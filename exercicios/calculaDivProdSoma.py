'''Fazer um programa que lê um número inteiro positivo n e imprime a divisão do produto dos n primeiros  números  positivos  pela  soma  dos  n  primeiros  números  positivos.  Usar  as  funções elaboradas nos exercícios 3 e 4.'''

print("==========================")
print("")
print("Programa que calcula a divisão entre produto e soma")
#======================================
def entradaDados():
    print("")
    print("==========================")
    n = int(input("Digite um número:"))
    print("")
    return n
#======================================
def controlador(n):
    div = n
    cont = n
    soma = 0
    prod = 1
    while cont != 0:
        soma = soma + n
        prod = prod * n
        cont = cont - 1
    result = (soma + prod)/div
    return result
#=======================================
def imprimir(result):
    print("")
    print("=====================")
    print(f"o resultado é: {result}")
#=======================================
# Programa Principal 
entrada = entradaDados()
processamento = controlador(entrada)
saida = imprimir(processamento)

