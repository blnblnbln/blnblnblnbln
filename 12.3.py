n = -1
while n < 0:
    n = int(input('Ingrese un valor: '))
suma2 = 0
for i in range(2,n+1):
    suma = 0
    for a in range(2,i):
        if i%a == 0:
            suma += 1
    if suma == 0:
        suma2 += 1
        print('el número', i, 'es primo')
        
print(suma2)
            
