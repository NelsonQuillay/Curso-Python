import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos de forma grafica
import seaborn as sns #libreia de graficos estadisticos

df = pd.read_csv("archivos_graficos\\dispersion.csv")
#print(df)

#print(df.columns)
#creando el grafico
sns.scatterplot(x='tiempo', y="dinero", data=df) #barplot indica que es un grafico de dispersion

plt.show() #con este metodo mostramos el grafico 