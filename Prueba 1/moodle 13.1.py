a = 1
b = 2
suma = 0
while a < b:
    a = int(input('Ingrese un valor: '))
    b = int(input('Ingrese un valor: '))
for c in range (b , a+1):
    if c%2 == 0 and c != 0:
        suma += 1

print('En dicho rango hay', suma, 'números pares')
