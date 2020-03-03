'''
Leer un valor por teclado (N)
Leer N valores por teclado y guardarlos en una lista
Calcular la suma de los valores de una lista
Calcular el promedio de los valores de una lista.
'''

N = int(input('Ingrese un valor para N= '))
lista = [ ]
for i in range (N):
    valor = int(input('Ingrese un valor: '))
    lista.append(valor)
    
suma = 0
for indice in range (N):
    valor = lista [indice]
    suma += valor
print(suma)