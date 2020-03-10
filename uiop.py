from random import randint

lista = [randint(1,25) for i in range (8)]
print(lista)

with open('pares.txt', 'w') as archivo:
    for i in lista:
        if (i%2 == 0):
            archivo.write(str(i) + ' ')
            

with open('pares.txt', 'r') as archivo:
    contenido = archivo.read()

print(contenido)