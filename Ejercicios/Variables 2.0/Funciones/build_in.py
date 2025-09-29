numeros = [3,7,10,4,99,75]

numero_mas_alto = max(numeros) #sirve para buscar en listas, tuplas y conjuntos
#print(numero_mas_alto)

numero_mas_bajo = min(numeros)
#print(numero_mas_bajo)


#redondeando
numero = round(12.35489556)
#print(numero) #12

numero = round(12.35489556 * 100)
#print(numero / 100) #12.36

numero = round(12.3519556,3) #el numero despues de  la coma, va a ser el decimal que vamos a obtener en el resultado.
#print(numero) #12.352


#devuelve False -> 0, vacio, False y ninguno (None) / True -> distinto a 0, True, cadena o datos no vacios
resultado_bool = bool(0) #False
resultado_bool = bool([]) #False
resultado_bool = bool(()) #False
resultado_bool = bool(False) #False
resultado_bool = bool(None) #False
resultado_bool = bool([125,4568]) #True
resultado_bool = bool('nelson') #True
#print(resultado_bool)


#devuelve True, si todos los elementos son verdaderos
resultado_all = all([1,'nelson', True,[1,9965]]) #True
resultado_all = all([0,'nelson', True,[1,9965]]) #False
#print(resultado_all)


#sumando todos los valores de un iterable
suma_total = sum(numeros) #198
print(suma_total)
