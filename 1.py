h = int(input('Ingrese un valor de hora: '))
m = int(input('Ingrese un valor de minuto: '))
s = int(input('Ingrese un valor de segundo: '))

hs = h*3600
ms = m*60

t = hs + ms + s
print(t)