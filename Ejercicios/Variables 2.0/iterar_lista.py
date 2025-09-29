#esto funciona tanto para listas[], tuplas() y conjuntos{}

animales = ['gato', 'perro', 'loro', 'cocodrilo']
numeros = [1, 2, 3, 4]

#recorriendo la lista de animales
for animal in animales:
    print(f' ahora la variable es: {animal}')


for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos lista del mismo tamaño y al mismo tiempo.
for animal, numero in zip(animales, numeros):
    print(f'recorriendo lista 1: {animal}')
    print(f'recorriendo lista 2: {numero}')


for num in range(10, 20):
    print(num)# 10 al 20

for num1 in range(10):
    print(num1)#0 al 10

#la forma correcta xe recorrer una lista con su indice
for num2 in enumerate(numeros):
    print(num2)
    #(0, 1)
    #(1, 2)
    #(2, 3)
    #(3, 4)
    print(num2[0]) # si queremos acceder al indice
    print(num2[1]) # si queremos acceder al valor

    indice = num2[0]
    valor = num2[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    #el indice es: 0 y el valor es: 1

#usando el for else
for num3 in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {num3}')
else:
    print('El bucle termino ')