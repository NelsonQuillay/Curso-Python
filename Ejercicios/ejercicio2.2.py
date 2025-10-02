#creando una funcion que nos devuelva numeros primos entre 0 y el aegumento que se pase

def es_primos(num):
   #for i in range(2, num-1): #2 i arranca valeindo 2 hasta num - 1
    for i in range(2, int(num**0.5)+1):
        if num%i == 0 : return False
    return True

def primos_hasta(num):
    primo = []
    for i in range(2, num +1):
        resultado = es_primos(i)
        if resultado == True: primo.append(i)
    return primo

resultado = primos_hasta(17)
print(resultado)

