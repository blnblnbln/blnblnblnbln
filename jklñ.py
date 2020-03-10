from random import randint
lista = [randint(1,10) for i in range(6)]
print(lista)

lista.sort()
print(lista)

n = len(lista)

lista2 = sorted(lista[n//2 : n], reverse = True)
print(lista2)

indice = 0
for i in range ( n//2 , n ):
    valor = lista2[indice]
    lista [i] = valor
    indice += 1
    
print(lista)