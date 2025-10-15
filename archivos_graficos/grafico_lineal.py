import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos de forma grafica
import seaborn as sns #libreia de graficos estadisticos

df = pd.read_csv("archivos_graficos\\comer.csv")
#print(df)

#creando el grafico
sns.lineplot(x="fecha", y="comer", data=df)

plt.plot("01-07", 17, "o") #indicamos de forma manual el valor mas alto con un punto

plt.show() #con este metodo mostramos el grafico 