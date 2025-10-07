with open("Ejercicios\\archivos\\texto_hola_mundo.txt","a") as archivo:
    #agregando el archivo
    #archivo.write("nos fuimos") 

    #usando un buclew para agregar lineas
    for i in range(5):
        archivo.write(f'linea {i+1} agregando\n')
