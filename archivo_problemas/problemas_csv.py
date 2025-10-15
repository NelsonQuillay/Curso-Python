#cambiar de tipo de datos de una columna
import pandas as pd
df = pd.read_csv("archivo_problemas\\datos.csv")
#print(df)

#convertir a string los datos cde una columna
df['edad'] = df['edad'].astype(str)
#print(type(df['edad'][0]))

#reemplazando los datos quillay por cuchi_cuchi
df['apellido'].replace('quillay', 'cuchi_cuchi', inplace=True)
#print(df['apellido'])

#eliminando las filas con datos vacios
df = df.dropna() #-> df = df.dropna(axis=0) es para eliminas las filas con datos faltantes
df = df.dropna(axis=1) #es para eliminas las columnas con datos faltantes

#eliminar las filas repetidas
df = df.drop_duplicates()

#creando un scv con el dataframe resultante (limpio)
df.to_csv("archivo_problemas\\datos_limpio.csv")
