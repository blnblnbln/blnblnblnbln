n = int(input('Ingrese un valor :'))
suma = 0
for a in range (1,n):
    if n%a == 0:
        suma += a
if suma == n:
    print('El valor es un número perfecto')
else:
    print('El valor no es un número perfecto')
