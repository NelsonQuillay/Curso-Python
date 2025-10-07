with open("Ejercicios\\archivos\\texto_hola_mundo.txt","w") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("gollll de media cancha") #"w" si no encuentra el archivo lo crea

    #agregando lineas con writelines
    archivo.writelines(["hola maestro\n", "golllllll\n"])
