'''def suma(a, b):
    return a + b

resultado = suma(1, 3)
print(resultado)'''


#usando el parametro args

'''def suma(*numeros):
    return sum(numeros)

resultado = suma(10, 10, 10)
print(resultado) #30'''

#utilizando el operador * como parametro (*args)
def suma(nombre, *numeros): #-> desventaja que no se puede agregar mas parametros depues del *
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado = suma('Nelson', 10, 10, 10)
print(resultado) #Nelson, la suma de tus numeros es: 30


def suma_tota(numeros): 
    return sum([*numeros])

resultado2 = suma_tota([10, 10, 10]) #de esta forma es mas optima pero se debe pasar una lista
print(resultado2)#30