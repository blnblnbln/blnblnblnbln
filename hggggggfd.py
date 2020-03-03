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

def calcular_suma(lista):
    suma = 0
    for indice in range (N):
        valor = lista [indice]
        suma += valor
    return suma

sumatoria = calcular_suma(lista)

def calcular_promedio(lista):
    suma = calcular_suma(lista)
    promedio = suma / len(lista)
    return promedio
    
promedio = calcular_promedio(lista)
print (sumatoria)
print(promedio)