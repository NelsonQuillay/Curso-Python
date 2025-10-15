import pandas as pd
import matplotlib.pyplot as plt #libreria de visualizacion de datos de forma grafica
import seaborn as sns #libreia de graficos estadisticos

df = pd.read_csv("archivos_graficos\\caja.csv")
#print(df)


#PARA LEER ARCHIVOS MAS GRANDES
'''def read_csv_in_chunks(file):
    for i,   chunk in enumerate(pd.read_csv(file, chunksize=1000)):
        print("Chunk #{}", format(i))
        print(chunk)
read_csv_in_chunks("big_file.csv")'''

#print(df.columns)
#creando el grafico
sns.boxplot(x='categoria', y="valor", data=df) #barplot indica que es un grafico de barras

plt.show() #con este metodo mostramos el grafico 