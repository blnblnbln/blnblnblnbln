'''
1. *[24 puntos]*
Cree una función que retorne la cantidad de películas por año
y el promedio de valoración por año,
considerando como valores extremos el menor año y el mayor año.
'''

archivo = open("top250_imdb.txt","r",encoding="utf-8")


def sumar(lista,ano):
    if ano not in lista:
        lista[ano] = 0
    if ano in lista:
        lista[ano] += + 1

columna = archivo.readline().strip()
columna = archivo.readline().strip()
columna = archivo.readline().strip()
#print(columna)

lista = {}
while columna != '':
    separar = columna.split('|')
    
    rut = int(separar[0])
    id_movie = str(separar[1])
    posicion = int(separar[2])
    ano = int(separar[3])
    votos = int(separar[4])
    #print(rut)

    sumar(lista,ano)

    
    #print(ano)    
    columna = archivo.readline().strip()


print(lista)