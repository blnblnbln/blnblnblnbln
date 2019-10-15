n = 1001
for i in range(1,n):
    suma = 0
    for a in range (1,i):
        if i%a == 0:
            suma += a
    if suma == i:
        print(i)
    #else:
    #    print('El valor no es un número perfecto')
