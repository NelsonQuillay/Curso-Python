frutas = ['banana', 'manzana', 'ciruela', 'pera', 'naranja', 'granada', 'duranzo']
cadena = 'Hola Nelson'
numeros = [2, 4, 8, 12]

for fruta in frutas:
    if fruta == 'granada':
        continue #en este caso detecta la granada, NO la devuelve y continua con el codigo.
    print(fruta)

for fruta1 in frutas:
    if fruta1 == 'pera':
        break #en este caso detecta la pera, NO la devuelve y detiene el bucle.
    print(fruta1)

for fruta2 in frutas:
    print(fruta2)
    if fruta2 == 'pera':
        break #en este caso detecta la pera, SI la devuelve y detiene el bucle.

else: #el else luego de un break no se ejecuta
    print('buble terminado')

#recorrer una cadena de texto
for letra in cadena:
    print(letra)


#for en una sola linea de codigo
numeros_diplicados = [x*2 for x in numeros]
print(numeros_diplicados)