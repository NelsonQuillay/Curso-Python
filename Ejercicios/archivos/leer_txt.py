archivo_sin_leer = open("Ejercicios\\archivos\\texto_hola_mundo.txt")

#leer el archivo completo
archivo = archivo_sin_leer.read()

#leer linea por linea
#lineas = archivo_sin_leer.readlines() #lee todas las lineas pero lo devuelve en un texto plano dividido por \n
#linea = archivo_sin_leer.readline() #lee solamente la primera linea
#linea = archivo_sin_leer.readline(10) #lee la cantidad de caracteres que le se paso

#cerrar el archivo
archivo_sin_leer.close()


#print(archivo_sin_leer.read())#si esta cerrado el archivo no se puede leer de nuevo,a menos que se vuelva a colocar open

print(archivo)