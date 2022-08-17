print("======================")
print("Calculadora Simples")
print("======================")


# ---------------------------------------------------

def entradaDados():
    print("")
    print("===========================")
    print("*- Entrada de Dados -*")
    n = int(input("Digite o número desejado:"))
    return n


# ---------------------------------------------------

def menu():
    print("*- Menu -*")
    print("==================")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("==================")
    op = int(input("Escolha uma opção:"))
    print("==================")
    return op


# ---------------------------------------------------

def adicao(n1, n2):
    print("1- Adição")
    s = n1 + n2
    return s


# ---------------------------------------------------

def subtracao(n1, n2):
    print("2- Subtração")
    sub = n1 + n2
    return sub


# ---------------------------------------------------

def multiplicacao(n1, n2):
    print("3- Multiplicação")
    m = n1 * n2
    return m


# ---------------------------------------------------

def divisao(n1, n2):
    print("4- Divisão")
    d = n1 / n2
    return d


# ---------------------------------------------------

def imprimir(result):
    print("*- Imprimindo Resultado...")
    print(f"resultado: {result}")


# ---------------------------------------------------

def controlador(n1, n2, op):
    print("")
    print("==================")
    print("*- Controlador -*")
    print("==================")
    if op == 1:
        r = adicao(n1, n2)
    elif op == 2:
        r = subtracao(n1, n2)
    elif op == 3:
        r = multiplicacao(n1, n2)
    elif op == 4:
        r = divisao(n1, n2)
    else:
        r = "opção inválida"
    return r


# ---------------------------------------------------
# Programa Principal

op = menu()
n1 = entradaDados()
n2 = entradaDados()
result = controlador(n1, n2, op)
imprimir(result)