import pandas as pd
#print(type(pd))
df = pd.read_csv("Ejercicios\\archivos\\datos.csv") #("Ejercicios\\archivos\\datos.csv", name = ["name", "lastname", "age"])
df2 = pd.read_csv("Ejercicios\\archivos\\datos.csv")

#obtengo todos los nombre de la columna
nombres = df["nombre"] 

'''cadena = "0123456789"
print(cadena[3:8]) #slice : -> devuelve 34567 de cadena'''

# ordenando dataframe por la edad -> menor a mayor o 'A' a la 'Z'
df_ordenado = df.sort_values('edad')
#print(df_ordenado)

#ordenar de forma descendente -> de mayor a menor o 'Z' a la 'A'
df_ordenado_desc = df.sort_values('edad', ascending=False)
#print(df_ordenado_desc)

#concatenando los dos dataframes
df_concatenado = pd.concat([df, df2])
#print(df_concatenado)

#accediendo a las primeras filas con head()
primeras_filas = df.head(3) # se accedio a las primeras 3 filas
#print(primeras_filas)

#accediendo a las ultimas filas con tail()
ultimas_filas = df.tail(3) # se accedio a las ultimas 3 filas
#print(ultimas_filas) 


#accediendo a la cantidad de filas y columnas con shape
'''#filas_y_columnas = df.shape
#print(filas_y_columnas) #devuelce 4(filas), 3(columnas)

#filas_totales = filas_y_columnas[0]
#print(filas_totales) #devuelve 4, que es la cantidad de filas 

#columnas_totales = filas_y_columnas[1]
#print(columnas_totales) #devuelve 3, que es la cantidad de columnas'''

filas_totales, columnas_totales = df.shape
#print(filas_totales)#devuelve 4
#print(columnas_totales) #devuelve 3

#obteniendo data estadistica del dataframe
df_info = df.describe()
#print(df_info)
'''count   4.000000
mean   20.750000
std    17.670597
min     4.000000
25%     6.250000
50%    21.000000
75%    35.500000
max    37.000000'''

#accediendo al apellido del df de la fila 3 con loc
elemento_especifico_loc = df.loc[2,'apellido'] #indicamos item 2, luego la columna
#print(elemento_especifico_loc)#devuelve quiroga

#accediendo al apellido del df de la fila 3 con iloc
elemento_especifico_iloc = df.iloc[2,1]
#print(elemento_especifico_iloc)#devuelve quiroga

#accediendo todos los datos de la fila 3 con loc
fila_3 = df.loc[2,:]
#print(fila_3)
'''nombre       melina
apellido    quiroga
edad             35
Name: 2, dtype: object'''

#accediendo a todos los nombre con iloc
nombres = df.iloc[:,0]
#print(nombres)
'''0    nelson
1    máximo
2    melina
3    álvaro
Name: nombre, dtype: object'''

#accediendo a las filas con edad mayores de 30
mayores_de_30 = df.loc[df["edad"]>30,:] #el primer dato que pide en la fila y segundo en la columna
print(mayores_de_30)
'''0  nelson  quillay    37
2  melina  quiroga    35'''