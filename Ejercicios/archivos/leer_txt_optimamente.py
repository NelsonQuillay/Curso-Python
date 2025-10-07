with open("Ejercicios\\archivos\\texto_hola_mundo.txt") as archivo:
    
    contenido = archivo.read()

    print(contenido)

# no es necesario cerrarlo al utilizar with open