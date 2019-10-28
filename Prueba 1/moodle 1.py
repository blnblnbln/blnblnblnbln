'''

Realice un programa que lea por teclado tres números enteros positivos (H, M, S) que contienen hora(s), minuto(s) y segundo(s) respectivamente, y calcule y muestre el tiempo en segundos.

'''

h = int(input('Ingrese un valor de hora: '))
m = int(input('Ingrese un valor de minuto: '))
s = int(input('Ingrese un valor de segundo: '))

hs = h*3600
ms = m*60

t = hs + ms + s
print(t)