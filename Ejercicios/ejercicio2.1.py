#pedir el nombre y la edad de los compañeros que vinieron a clases

#funcion para obtener al asistente y al proferon segun su edad.
def obtener_compañero(cantidad_de_compañeros):

    #crear la lista con los compañeros
    compañeros = []

    #ejecutar el for para pedir la info a todos los compañeros
    for i in range(cantidad_de_compañeros):
        nombre = input('Ingrese el nombre del compañero: ')
        edad = int(input('Ingrese la edad del compañero: '))
        compañero = (nombre, edad)

        #agregar la info a la lista
        compañeros.append(compañero)

    #ordenar de menor a m ayor segun la edad
    compañeros.sort(key= lambda x:x[1])

    #compañero[x] devuelve una tupla con (nombre y edad) y despues accedemos al nombre
    asistente = compañeros [0][0]
    profesor = compañeros [-1][0]

    #retornamos una tupla
    return asistente, profesor

#desempaquetamos lo que nos retorna la funcion 
asistente, profesor = obtener_compañero(5)

# mostrar el resultado
print(f'el profesor es {profesor} y el asistente es {asistente}')
