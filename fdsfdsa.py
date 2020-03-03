matriz = []
M = int(input('Ingrese la cantidad de filas: '))
N = int(input('Ingrese la cantidad de columnas: '))

for i in range (M):
    matriz.append([])
    for j in range (N):
        valor = int(input('Ingrese un valor: '))
        matriz[i].append(valor)
print(matriz)

suma=0
for i in range (M):
    for j in range (N):
        valor = matriz[i][j]
        suma += valor

print(suma)
    
