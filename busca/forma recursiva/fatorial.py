#fatorial (recursive)

#5! --> 5*4*3*2*1 = 120

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
#principal
n = int (input("Digite o número:"))
print(f'Fatorial de {n} é: {fatorial(n)}' )