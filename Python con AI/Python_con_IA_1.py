#print("Hola, Cursor")

'''for i in range(5):

    print(i)
'''

'''# Calcular el factorial de un número dado
def factorial (n):
    
    #Si n es 0 o 1, devolver 1 (caso base)
    #En otro caso, devolver n * factorial(n-1)
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(6))'''

'''# Imprimir la secuencia de Fibonacci hasta el n-ésimo término

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))     
'''
def suma_lista(lista: list) -> int:
    total = 0
    for elemento in lista:
        total += elemento
    return total

print(suma_lista([1, 2, 3, 4, 5]))  