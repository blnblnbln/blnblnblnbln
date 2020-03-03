def funcion(A, B):
    suma = 0
    for i in range (A, B+1):
        suma += i
    return suma

A = int(input('Ingrese valor de A: '))
B = int(input('Ingrese valor de B: '))
resultado = funcion (A, B)
print(resultado)