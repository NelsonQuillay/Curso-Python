import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos de forma grafica
import seaborn as sns #libreia de graficos estadisticos

df = pd.read_csv("archivos_graficos\\ingresos.csv")
#print(df)

#print(df.columns)
#creando el grafico
sns.barplot(x='trabajos', y="ingresos", data=df) #barplot indica que es un grafico de barras

#obteniendo el total del ingreso
total_ingresos = df['ingresos'].sum()

#mostrando el total
print(f"El total del ingreso es de: ${total_ingresos}")

plt.show() #con este metodo mostramos el grafico 