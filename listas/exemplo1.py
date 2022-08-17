lista = [2,10,5,-3,20]

def imprimeElementos():
    i=0
    while i < len(lista):
        print(f'Elemento: {lista[i]}')
        i+=1
        lista[0] = 2000
#--------------------------------------
#Programa Principal

imprimeElementos()
print("-------------")
imprimeElementos()

#--------------------------------------
