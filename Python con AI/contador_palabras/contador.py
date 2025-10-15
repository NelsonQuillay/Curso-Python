 # Programa para contar palabras en un archivo de texto
archivo = input("Open_academy\\Python_con_AI\\contador_palabras\\nombres_y_apellidos.txt")

try:
    with open(archivo, "r", encoding="utf-8") as f:
        texto = f.read()

except FileNotFoundError:
    print(f"El archivo {archivo} no existe.")
    exit(1)


# Separar el contenido en palabras
import re
palabras = re.findall(r"\w+", texto.lower())

total_palabras = len(palabras)

print(f"El archivo {archivo} tiene {total_palabras} palabras.")

# Contar frecuencias

from collections import Counter 

frecuencia = Counter(palabras)

mas_comunes = frecuencia.most_common(10)
print("\nPalabras más frecuentes:")

for palabra, frecuencia in mas_comunes:
    print(f"{palabra}: {frecuencia}")
