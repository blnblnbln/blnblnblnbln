'''

Realice un programa que determine si un número entero positivo es perfecto.
Un número es perfecto si es igual a la suma de todos sus divisores positivos sin incluir el propio número.
Por ejemplo, el número 6 es perfecto. El 6 tiene como divisores: 1, 2, 3 y 6 pero el 6 no se cuenta como divisor para comprobar si es perfecto. Si sumamos 1 + 2 + 3 = 6.

'''

N = int(input("Ingrese un valor: "))
suma = 0

for a in range (1,N):
    if N%a == 0:
        suma += a
if suma == N:
    print("El valor es un número perfecto")
    
else:
    print("El valor no es un número perfecto")