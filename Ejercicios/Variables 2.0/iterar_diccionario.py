diccionario = {
    'nombre': 'Nelson',
    'apellido': 'Quillay',
    'edad': 37
}

for key in diccionario:
    print(key)#muestra la clave


#recorriendo diccionario con la funcion item() para obtener clave: valor 
for key1 in diccionario.items():
    print(key1)#muestra la clave: valor en una tupla