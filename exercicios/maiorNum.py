"""Escreva um programa que leia dois números do teclado (x e y), verifique qual é o maior  e  imprima  a  mensagem:  “o  número  {x}  é  maior  do  que  {y}.  O  programa deve ter:
•Função para entrada de dados
•Função para verificar o maior número lido
•Função para imprimir a mensagem
•Programa Principal para testar as funções acima"""

print("Calcula o maior número")
print("======================")

def entradaDados():
    print("Digite dois números para saber qual é maior")
    print("===========================================")
    n = int(input("digite o número:"))
    return n
#=======================================================
def controlador(n1,n2):
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    return maior
#=======================================================
def imprimir(result):
    print(f"o maior número é {result}")
#=======================================================
# Programa principal

n1 = entradaDados()
n2 = entradaDados()
processo = controlador(n1,n2)
imprimir(processo)
