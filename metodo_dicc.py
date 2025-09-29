# Metodo diccionario clases

diccionario = {
    "nombre" : 'Nelson',
    "apellido" : 'Quillay',
    "subs" : 1000000
}

valor = diccionario.get('nombre') #diccionario[0] si get no encuentra clave devuelva None.
clave = diccionario.keys() #nos devuelve un obj dict_iutrem

#elimina todo el diccionario
#diccionario.clear()

#elimina un elemento del diccionario
diccionario.pop('nombre', 'subs')

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)