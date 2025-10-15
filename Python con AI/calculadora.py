#Pide al usuario una operación (suma, resta, multiplicación, división) y dos números.
#Ejecute la operación y muestre el resultado.
#Debe repetirse hasta que el usuario escriba "salir" como operación.

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b

# Loop principal que se repite hasta que el usuario escriba "salir"
while True:
    operacion = input('Ingrese el nombre de la operacion deseada (suma, resta, multiplicacion, division) o "salir" para terminar: ')
    
    # Verificar si el usuario quiere salir
    if operacion.lower() == 'salir':
        print('¡Hasta luego!')
        break
    
    # Pedir los números solo si no es "salir"
    try:
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        
        # Realizar la operación
        if operacion == 'suma':
            resultado = suma(a, b)
            print(f'El resultado de {a} + {b} = {resultado}')
        elif operacion == 'resta':
            resultado = resta(a, b)
            print(f'El resultado de {a} - {b} = {resultado}')
        elif operacion == 'multiplicacion':
            resultado = multiplicacion(a, b)
            print(f'El resultado de {a} * {b} = {resultado}')
        elif operacion == 'division':
            if b != 0:  # Evitar división por cero
                resultado = division(a, b)
                print(f'El resultado de {a} / {b} = {resultado}')
            else:
                print('Error: No se puede dividir por cero')
        else:
            print('Operacion no valida. Intente de nuevo.')
            
    except ValueError:
        print('Error: Por favor ingrese números válidos.')
    
    print()  # Línea en blanco para separar operaciones     


