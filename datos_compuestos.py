#list
lista = ['nelson', 'quillay', True, 1988]

#tupla
tupla = ('nelson', 'quillay', True, 1988) #la tupla no se puede modificar

print(lista)
print(lista[1])
print(tupla[1]) #para mostar todo va con []

# conjunto (set)
conjunto = {'nelson', 'quillay', True, 1988} #no deja repetir valores #no se puede acceder a los elementos por su indice

print(conjunto)

#diccionario (dict)
diccionario = {
    'nombre': 'Nelson',
    'apellido': 'Quillay',
    'edad': 36,
    'argentino': True
}
print(diccionario['nombre'])