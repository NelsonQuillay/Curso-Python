frase = input('decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)

print('----------------------------------------------------------------------------------------------')
if cantidad_de_palabras > 120: #para que no supere el minuto de la frase
    print('se supero el limite de palabras')

print('----------------------------------------------------------------------------------------------')
print(f'dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'dalto lo diria en {cantidad_de_palabras * 100 // 2 * 0.7 / 100} segundos en decirlo')
