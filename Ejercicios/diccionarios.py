#creando diccionario  con dict()
diccionario = dict(nombre = 'nelson', apellido = 'quillay') #con dict() podemos crear diccionarios vacios

#la tupla puede ser clave
diccionario1 = {('dato1', 'dato2') : 'dato3'}

#la lista NO puede ser clave
#diccionario2 = {['dato1', 'dato2'] : 'dato3'} #error

#se debe utiliza frozenser para poder utilizar lista en claves
diccionario3 = {frozenset(['dato1', 'dato2']) : 'dato3'}  

#crear diccionario con fromkeys() es un metodo de diccionarios
diccionario4 = dict.fromkeys(['nelson', 'quillay']) #se debe crear una lista para que le valor nos revuelva None

print(diccionario4)