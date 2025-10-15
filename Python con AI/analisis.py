import pandas as pd

#Calcula estadísticas simples: media, mediana, desviación estándar de cada columna.

df = pd.read_csv('Open_academy\\Python_con_AI\\datos_limpio.csv')   #creamos el dataframe

#calcula la media de la columna edad
media_edad = df['edad'].mean()
print(f"La media de la columna edad es: {media_edad}")

#Calcula la media de la columna estatura
media_estatura = df['estatura'].mean()
print(f"La media de la columna estatura es: {media_estatura}")

#Calcula la mediana de la columna edad
mediana_edad = df['edad'].median()
print(f"La mediana de la columna edad es: {mediana_edad}") 

#calcula la mediana de la columna estatura
mediana_estatura = df['estatura'].median()
print(f"La mediana de la columna estatura es: {mediana_estatura}")

#calcula la desviacion estandar de la columna edad
desviacion_estandar_edad = df['edad'].std()
print(f"La desviacion estandar de la columna edad es: {desviacion_estandar_edad}")

#calcula la desviacion estandar de la columna estatura
desviacion_estandar_estatura = df['estatura'].std()
print(f"La desviacion estandar de la columna estatura es: {desviacion_estandar_estatura}")
