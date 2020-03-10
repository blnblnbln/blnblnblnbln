from random import randint

lista = [randint(1,24) for i in range (8)]
print(lista)

lista.sort()
print(lista)

lista.sort(reverse = True)
print(lista)