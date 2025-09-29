'''def multiplicar_por_dos(x):
    return x*2'''

#lambda crea funciona anonimas que luego se pueden guardar en variables
multiplicar_por_dos = lambda x : x*2


numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

'''#creando una funcion comun que me diga si el numero es par o no
def es_par(num):
    if(num % 2 ==0):
        return True
    
#usamos filter con una funcion comun
numeros_pares = filter(es_par, numeros)'''

#creando lo mismo pero con lambda

numeros_pares = filter(lambda num: num%2 == 0, numeros )
print(list(numeros_pares))