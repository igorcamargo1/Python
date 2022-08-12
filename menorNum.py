'''Fazer uma função que tem como parâmetro de entrada três números inteiros a, b, c e fornece como saída o menor dentre os três números.'''

print("====================")
print("Calcula menor número")
print("====================")
print("")
#=======================================
def entradaDados():
    print("===========================")
    n = int(input("Digite um número:"))
    print("")
    return n
#========================================
def controlador(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3
    return menor
#==========================================
def imprimir(result):
    print("============================")
    print("")
    print(f"o menor número é: {result}")
    print("")
    print("=============================")
#==========================================
# Programa Principal 

n1 = entradaDados()
n2 = entradaDados()
n3 =  entradaDados()
processamento = controlador(n1,n2,n3)
saida = imprimir(processamento)
    
