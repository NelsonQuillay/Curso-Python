#Tipos de datos básicos
#En Python, los tipos de datos básicos son las categorías en las que se pueden clasificar los valores que utilizamos en nuestros programas. Comprender los diferentes tipos de datos es fundamental para trabajar con variables y realizar operaciones en Python. Los tipos de datos básicos incluyen:

#Enteros (int)
#Los números enteros son aquellos que no tienen parte decimal. En Python, se representan simplemente escribiendo el número sin comillas ni puntos decimales. Por ejemplo:

'''edad = 25
cantidad = 100'''
 

#Flotantes (float)
#Los números flotantes, también conocidos como números de punto flotante, son aquellos que tienen una parte decimal. En Python, se representan utilizando un punto para separar la parte entera de la parte decimal. Por ejemplo:

'''precio = 9.99
altura = 1.75'''
 

#Cadenas de texto (strings)
#Las cadenas de texto, o simplemente cadenas, son secuencias de caracteres encerradas entre comillas simples ('...') o dobles ("..."). Se utilizan para representar texto en Python. Por ejemplo:

'''nombre = "Juan"
mensaje = '¡Hola, mundo!'''
#Puedes incluir caracteres especiales en las cadenas utilizando el carácter de escape \. Por ejemplo, para incluir comillas dentro de una cadena, puedes usar \' o \". También puedes utilizar la notación de triple comilla ('''...''' o """...""") para crear cadenas de varias líneas.

 

#Booleanos
#Los valores booleanos representan los valores de verdad: True (verdadero) y False (falso). Se utilizan comúnmente en expresiones condicionales y operaciones lógicas. Por ejemplo:

'''es_mayor_de_edad = True
tiene_descuento = False
'''

#Variables
#Las variables son contenedores que nos permiten almacenar y manipular datos en nuestros programas. Puedes pensar en una variable como una etiqueta a la que asignas a un valor específico. En Python, no es necesario declarar el tipo de datos de una variable de antemano, ya que Python infiere el tipo de datos automáticamente en función del valor asignado.

 

#Declaración y asignación de variables
#Las variables son contenedores que nos permiten almacenar y manipular datos en nuestros programas. Para declarar y asignar un valor a una variable en Python, utilizamos el operador de asignación =. El nombre de la variable va a la izquierda del operador, y el valor que deseas asignar va a la derecha. Por ejemplo:
'''
nombre = "Juan"
edad = 25
altura = 1.75
es estudiante = True
'''
#En el ejemplo, hemos declarado y asignado valores a las variables nombre, edad, altura y es_estudiante. Python infiere automáticamente el tipo de datos de cada variable en función del valor asignado.
#También puedes asignar el mismo valor a múltiples variables en una sola línea utilizando el operador de asignación múltiple:
'''
a = b = c = 10
'''
#En este caso, las variables a, b y c tendrán el valor 10.

 

#Normas para nombrar variables
#Al nombrar variables en Python, es importante seguir algunas normas para mantener un código legible y evitar errores:

#Los nombres de las variables solo pueden contener letras (a-z, A-Z), números (0-9) y guiones bajos (_). No pueden comenzar con un número.
#Python distingue entre mayúsculas y minúsculas, por lo que nombre y Nombre son variables diferentes.
#No se pueden utilizar palabras clave reservadas de Python como nombres de variables (por ejemplo, if, else, for, while, etc.).
#Se recomienda utilizar nombres descriptivos para las variables, que indiquen claramente su propósito: nombre, edad, total_ventas, etc.

#Siguiendo estas normas, algunos ejemplos de nombres de variables válidos son:
'''
edad
nombre_completo
total_ventas
_contador
'''
#Y algunos ejemplos de nombres de variables inválidos son:
'''
1edad   # Comienza con un número
nombre-completo   # Utiliza un guion en lugar de un guion bajo
if   # Palabra clave reservada de Python
'''


#Operadores
#Los operadores son símbolos especiales que nos permiten realizar operaciones en variables y valores. Python proporciona diferentes tipos de operadores para realizar operaciones aritméticas, comparaciones y operaciones lógicas.

#Aritméticos
#Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas. Los principales operadores aritméticos en Python son:

#Suma (+): suma dos valores.
#Resta (-): resta el segundo valor del primero.
#Multiplicación (*): multiplica dos valores.
#División (/): divide el primer valor por el segundo y devuelve un resultado de tipo flotante.
#División entera (//): divide el primer valor por el segundo y devuelve un resultado de tipo entero (se descarta la parte decimal).
#Módulo (%): devuelve el resto de la división entre el primer valor y el segundo.
#Exponenciación (**): eleva el primer valor a la potencia del segundo.
#Ejemplos:
'''
a = 10
b = 3


suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000
'''
 

#De comparación
#Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (True o False) según el resultado de la comparación. Los operadores de comparación en Python son:

#Igual a (==): devuelve True si ambos valores son iguales.
#Diferente de (!=): devuelve True si los valores son diferentes.
#Mayor que (>): devuelve True si el primer valor es mayor que el segundo.
#Menor que (<): devuelve True si el primer valor es menor que el segundo.
#Mayor o igual que (>=): devuelve True si el primer valor es mayor o igual que el segundo.
#Menor o igual que (<=): devuelve True si el primer valor es menor o igual que el segundo.
#Ejemplos:
'''
a = 10
b = 3


igual = a == b   # False
diferente = a != b   # True
mayor que = a > b   # True
menor que = a < b   # False
mayor o igual = a >= b   # True
menor o igual = a <= b   # False
'''

#Lógicos
#Los operadores lógicos se utilizan para combinar expresiones condicionales y evaluar múltiples condiciones. Los operadores lógicos en Python son:

#AND (and): devuelve True si ambas condiciones son verdaderas.
#OR (or): devuelve True si al menos una de las condiciones es verdadera.
#NOT (not): invierte el valor de una condición, devuelve True si la condición es falsa y False si la condición es verdadera.
#Ejemplo:
'''
a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False
'''
#Puedes utilizar estos operadores para realizar cálculos, tomar decisiones basadas en comparaciones y combinar condiciones lógicas en tus programas.



#>Estructuras de control

#Estructuras condicionales
#Las estructuras condicionales nos permiten ejecutar diferentes bloques de código según se cumpla o no una determinada condición. En Python, las estructuras condicionales más utilizadas son if, if-else y if-elif-else.

#IF
#La estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es la siguiente:
'''
if condicion:

   # Bloque de código a ejecutar si la condición es verdadera
   instrucciones
'''
#Ejemplo:
'''
edad = 18

if edad >= 18:
   print ("Eres mayor de edad.")
'''
#En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad."

#IF-ELSE
#La estructura if-else nos permite especificar un bloque de código alternativo que se ejecutará si la condición del if es falsa. La sintaxis básica es la siguiente:
'''
edad = 15

if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")
'''
#En este ejemplo, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if y se imprimirá el mensaje "Eres mayor de edad." De lo contrario, se ejecutará el bloque de código dentro del else y se imprimirá el mensaje "Eres menor de edad."

 

#IF-ELIF-ELSE
#La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos. La sintaxis básica es la siguiente:

'''
if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones
'''

#Ejemplo:
'''
calificacion = 85

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")

'''
#En este ejemplo, se evalúan múltiples condiciones en orden. Si la variable calificación es mayor o igual a 90, se imprime "Excelente". Si no se cumple la primera condición, pero calificación es mayor o igual a 80, se imprime "Muy bueno". Si no se cumplen las condiciones anteriores, pero calificación es mayor o igual a 70, se imprime "Bueno". Si ninguna de las condiciones anteriores es verdadera, se ejecuta el bloque else y se imprime "Necesita mejorar".





#Bucles/loops

#For
#El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable. La sintaxis básica es la siguiente:
'''
for variable in secuencia:

    # Bloque de código a repetir
    instrucciones
'''    
#Ejemplo:
'''
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
'''
#En este ejemplo, el bucle for itera sobre la lista frutas. En cada iteración, la variable fruta toma el valor de un elemento de la lista, y se ejecuta el bloque de código dentro del bucle. En este caso, se imprime cada fruta en una línea separada.


#While
#El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:
'''
while condicion:

    # Bloque de código a repetir
    instrucciones
'''
#Ejemplo:
'''
contador = 0

while contador < 5:

    print(contador)
    contador += 1

'''
#En este ejemplo, el bucle while se ejecuta mientras la variable contador sea menor que 5. En cada iteración, se imprime el valor de contador y luego se incrementa en 1 mediante la instrucción contador += 1. El bucle se detendrá cuando contador alcance el valor de 5.

#Es importante tener cuidado al usar el bucle while, ya que, si la condición nunca se vuelve falsa, el bucle se ejecutará indefinidamente, lo que se conoce como un bucle infinito.


#VIDEO
'''
print("numero 1 al 5 *2 con for")

for numero in range (1, 6):

    print(numero*2)


print("/numero 1 al 5 *2 con for")

contador = 1
while contador <= 5:
    print (contador*2)
    contador +=1

    '''

#Control de bucles
#Python proporciona algunas instrucciones especiales para controlar el flujo de ejecución dentro de los bucles:
#Break
#La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición. Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución continúa con la siguiente instrucción fuera del bucle.
'''
contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break
'''
#En este ejemplo, el bucle while se ejecuta indefinidamente debido a la condición True. Sin embargo, dentro del bucle se utiliza una estructura condicional if para verificar si contador es igual a 5. Cuando se cumple esta condición, se ejecuta la instrucción break, lo que hace que el bucle se detenga y el flujo de ejecución continúe con la siguiente instrucción fuera del bucle.


#Continue
#La instrucción continue se utiliza para saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración.
#Ejemplo:
'''
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
'''
#En este ejemplo, el bucle for itera sobre los números del 0 al 9 utilizando la función range(). Dentro del bucle, se verifica si el número es divisible por 2 utilizando el operador de módulo %. Si el número es divisible por 2 (es decir, si es par), se ejecuta la instrucción continue, lo que hace que se salte el resto del bloque de código y se pase a la siguiente iteración del bucle. Como resultado, solo se imprimirán los números impares.

#Pass
#La instrucción pass es una operación nula que no hace nada. Se utiliza como marcador de posición cuando se requiere una instrucción sintácticamente, pero no se desea realizar ninguna acción.
#Ejemplo:
'''
for i in range(5):
    pass
'''
#En este ejemplo, el bucle for itera sobre los números del 0 al 4, pero no se realiza ninguna acción dentro del bucle debido a la instrucción pass. Esto puede ser útil cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante.

#Conclusión
#Las estructuras de control son herramientas poderosas que nos permiten controlar el flujo de ejecución de nuestros programas. Con las estructuras condicionales (if, if-else, if-elif-else) podemos tomar decisiones basadas en condiciones, mientras que con los bucles (for, while) podemos repetir bloques de código varias veces. Además, las instrucciones break, continue y pass nos brindan un control adicional sobre el comportamiento de los bucles.




#>Estructuras de datos

#Listas
#Una lista es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos. Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes [], separados por comas.

#Creación y acceso
#Para crear una lista, simplemente encierra los elementos entre corchetes:
'''
frutas = ["manzana", "banana", "naranja"]
'''

# Para acceder a los elementos de una lista, utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0.
'''
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"
'''
# También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.
'''
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"
'''

#Métodos de listas
#Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista. Algunos métodos comunes son:

#append(elemento): agrega un elemento al final de la lista.
#insert(indice, elemento): inserta un elemento en una posición específica de la lista.
#remove(elemento): elimina la primera aparición de un elemento en la lista.
#pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
#sort(): ordena los elementos de la lista en orden ascendente.
#reverse(): invierte el orden de los elementos en la lista.
#Ejemplo:

'''
frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

'''

#Listas de comprensión
#Las listas de comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente. Permiten filtrar y transformar los elementos de una lista en una sola línea de código.
'''
nueva_lista = [expresion for elemento in secuencia if condicion]
'''
#Ejemplo:
'''
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]
'''
#En este ejemplo, se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números pares de la lista numeros. La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.




#Tuplas
#Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. Los elementos de una tupla se encierran entre paréntesis (), separados por comas.
#Creación y acceso
#Para crear una tupla, encierra los elementos entre paréntesis:
'''
punto = (3, 4)
'''

#Para acceder a los elementos de una tupla, utiliza el índice del elemento entre corchetes, similar a las listas:
'''
print(punto[0])  # Imprime 3

print(punto[1])  # Imprime 4
'''


#Métodos de tuplas
#Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

#count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
#index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
#len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
'''
mi_tupla = (1, 2, 3, 2, 4, 2)

print (mi_tupla.count(2)) 
print (mi_tupla.index(2)) 
print (mi_tupla.index(2, 2))   
'''


#Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor. Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. Los diccionarios se encierran entre llaves {}, y los pares clave-valor se separan por comas.

#Creación y acceso
#Para crear un diccionario, utiliza llaves y separa las claves y valores con dos puntos.
#persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
#Para acceder a los valores de un diccionario, utiliza la clave correspondiente entre corchetes:
'''
print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"
'''
#También puedes utilizar el método get() para obtener el valor de una clave. Si la clave no existe, devuelve un valor predeterminado (por defecto, None).


#Métodos de diccionarios
#Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

#keys(): devuelve una vista de todas las claves del diccionario.
#values(): devuelve una vista de todos los valores del diccionario.
#items(): devuelve una vista de todos los pares clave-valor del diccionario.
#update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
#Ejemplo:
'''persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}'''



#Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una colección de elementos únicos. Los conjuntos se encierran entre llaves {} o se crean utilizando la función set().
#Creación y operaciones básicas
#Para crear un conjunto, utiliza llaves o la función set():
'''
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])
'''

#Los conjuntos admiten operaciones matemáticas de conjuntos, como la unión (|), la intersección (&), la diferencia (-) y la diferencia simétrica (^).

'''
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}
'''


#Métodos de conjuntos
#Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

#add(elemento): agrega un elemento al conjunto.
#remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
#discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
#clear(): elimina todos los elementos del conjunto.
#Ejemplo:

'''frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")

print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()'''

#Las estructuras de datos en Python nos brindan una gran flexibilidad y potencia para almacenar y manipular datos en nuestros programas. Las listas son útiles para colecciones ordenadas y mutables, las tuplas para colecciones ordenadas e inmutables, los diccionarios para almacenar pares clave-valor y los conjuntos para colecciones no ordenadas de elementos únicos.


#EVALUACION

'''numero = 7

if numero % 2 == 0:
    print("Par")

else:
    print("Impar")



edad = 20

if edad < 18:
    print("eres mayor de edad")

elif edad >= 18 and edad <60:
    print("eres un adulto")

elif edad == 60:
    print("feliz 60 años")
else:
    print("eres adulto mayor")

    # este es un comentario de una linea'''

'''def multiplicar (a, b):
     
    return a * b



resultado = multiplicar (5, 3) + multiplicar (2, 4)

print(resultado)'''



#Definición y llamada de funciones
#Para definir una función en Python, utilizamos la palabra clave def seguida del nombre de la función y paréntesis. Opcionalmente, podemos especificar parámetros dentro de los paréntesis. El bloque de código de la función se indenta después de los dos puntos.
#Para llamar a una función, simplemente escribimos el nombre de la función seguido de paréntesis:

'''def saludo():
    print("Hola, mundo!")

saludo()  # Imprime "¡Hola, mundo!"'''


#Parámetros y argumentos
#Las funciones pueden aceptar parámetros, que son valores que se pasan a la función cuando se la llama. Los parámetros se especifican dentro de los paréntesis en la definición de la función.

'''def saludo(nombre):
    print(f"Hola, {nombre}!")'''


#Al llamar a la función, proporcionamos los argumentos correspondientes a los parámetros:
'''
saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("Mario")  # Imprime "¡Hola, Mario!"'''

#Valores de retorno
#Las funciones pueden devolver valores utilizando la palabra clave return. El valor de retorno puede ser utilizado por el código que llama a la función. 
'''
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7
'''


#Funciones anónimas (lambda)
#Python permite crear funciones anónimas o funciones lambda, que son funciones sin nombre definidas en una sola línea. Se utilizan comúnmente para funciones pequeñas y concisas.

'''cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25'''


#Alcance de las variables (local vs. global)
#Las variables definidas dentro de una función tienen un alcance local, lo que significa que solo son accesibles dentro de la función. Por otro lado, las variables definidas fuera de cualquier función tienen un alcance global y pueden ser accedidas desde cualquier parte del programa.

'''def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función


variable_global = 20


def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar


funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
print(variable_local)  # Genera un error, la variable no está definida en este alcance.'''


#Documentación de funciones (docstrings)
#Es una buena práctica documentar nuestras funciones utilizando docstrings. Los docstrings son cadenas de texto que describen el propósito, los parámetros y el valor de retorno de una función. Se colocan inmediatamente después de la definición de la función y se encierran entre triples comillas dobles.

'''def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura'''

#Funciones con número variable de argumentos
#Python permite definir funciones que acepten un número variable de argumentos. Esto se logra utilizando el operador * antes del nombre del parámetro.


'''def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22'''
#Las funciones son una herramienta fundamental en la programación y nos permiten estructurar y modularizar nuestro código. Con la capacidad de definir funciones personalizadas, podemos encapsular tareas específicas y reutilizarlas en diferentes partes de nuestro programa.
#Además de las funciones definidas por el usuario, Python también proporciona una amplia gama de funciones incorporadas que podemos utilizar directamente, como print(), len(), range(), entre otras.




#Errores comunes en Python

#Error de sintaxis (SyntaxError)
#Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar dos puntos después de una declaración de función o un bucle.
'''def mi_funcion() # Falta los dos puntos
    print("Hola")'''


#Error de nombre (NameError)
#Ocurre cuando se hace referencia a una variable o función que no ha sido definida.

'''print(variable_no_definida)'''
 

#Error de tipo (TypeError)
#Ocurre cuando se realiza una operación con tipos de datos incompatibles, como intentar sumar un número y una cadena.

'''resultado = 5 + "10"'''
 

#Error de índice (IndexError)
#Ocurre cuando se intenta acceder a un índice fuera del rango válido de una lista o secuencia.

'''lista = [1, 2, 3]
print(lista[3])  # El índice 3 está fuera del rango'''



#Try
#El bloque try contiene el código que puede generar una excepción. Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.
'''try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")'''


#Except
#El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.
'''try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")'''



#Finally
#El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrió una excepción o no. Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.
'''try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción'''



#Para crear una excepción personalizada, debes crear una clase que herede de la clase base Exception o de una de sus subclases.
'''def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")


try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")'''
#En este ejemplo, se define una función llamada funcion(). Dentro de la función, se verifica una condición y, si se cumple, se genera una excepción utilizando la declaración raise. En lugar de crear una clase personalizada, se utiliza directamente la clase base Exception para generar la excepción.

#Luego, se utiliza un bloque try-except para capturar y manejar la excepción. La variable e se utiliza para acceder a la descripción del error proporcionada al generar la excepción.
#El manejo de errores y excepciones es una parte fundamental de la programación en Python. Te permite manejar situaciones inesperadas de manera controlada y evitar que tu programa se bloquee o se detenga abruptamente.
#Cuando ocurre un error en tu código, Python genera una excepción. Al utilizar bloques try-except, puedes capturar y manejar estas excepciones de manera adecuada. Puedes especificar diferentes bloques except para manejar distintos tipos de excepciones y realizar acciones específicas en cada caso.


#Entrada de datos del usuario
#Para obtener información del usuario durante la ejecución del programa, podemos utilizar la función input(). Esta función muestra un mensaje en la pantalla y espera a que el usuario ingrese un valor.

'''nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")'''
#En este ejemplo, se solicita al usuario que ingrese su nombre y edad utilizando la función input(). Los valores ingresados se almacenan en las variables nombre y edad, respectivamente. Luego, se utilizan estas variables para mostrar un saludo personalizado en la pantalla.


'''edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")'''
#En este ejemplo, se solicita al usuario que ingrese su edad y se convierte el valor ingresado a un número entero utilizando int(). Luego, se utiliza una estructura condicional para verificar si la edad es mayor o igual a 18 y mostrar un mensaje correspondiente.

#>Salida de datos
#Para mostrar información en la pantalla, utilizamos la función print(). Esta función toma uno o más argumentos y los muestra en la consola.

#Podemos utilizar la f-string (formateo de cadenas) para incrustar variables directamente dentro de una cadena de texto.
'''nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")'''
#En este caso, las variables se incrustan dentro de la cadena utilizando llaves {} y se precede la cadena con la letra f para indicar que es una f-string.


#Python nos permite leer y escribir datos en archivos externos. Podemos abrir archivos en diferentes modos, como lectura ("r"), escritura ("w") o anexar ("a"), y realizar operaciones de lectura y escritura.


#Lectura de archivos
#Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().

'''archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()'''

#En este ejemplo, se abre el archivo "datos.txt" en modo de lectura utilizando open(). Luego, se lee todo el contenido del archivo utilizando el método read() y se almacena en la variable contenido. Finalmente, se muestra el contenido en la pantalla y se cierra el archivo utilizando el método close().


#Escritura de archivos
#Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.

'''archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()'''

#En este ejemplo, se abre el archivo "datos.txt" en modo de escritura utilizando open(). Luego, se escribe la cadena "¡Hola, mundo!" en el archivo utilizando el método write(). Finalmente, se cierra el archivo utilizando el método close().


#También puedes utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática.

'''with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    '''
#En este caso, el archivo se abre utilizando la declaración with y se cierra automáticamente una vez que se sale del bloque with, incluso si ocurre una excepción.

#Importar módulos
#Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import. Podemos importar un módulo completo o funciones específicas de un módulo.

'''import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0'''

#En este ejemplo, se importa el módulo math utilizando la declaración import. Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.

#También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.

'''from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0'''

#En este caso, se importa solo la función sqrt() del módulo math, lo que nos permite utilizarla directamente sin tener que precederla con el nombre del módulo.



#>Funciones y clases de módulos estándar
#La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones y clases útiles. Algunos ejemplos comunes incluyen:

#Math
#Proporciona funciones matemáticas, como sqrt() (raíz cuadrada), sin() (seno), cos() (coseno), entre otras.

#Random
#Ofrece funciones para generar números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras.

#Datetime
#Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.


'''import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual'''


#Creación de módulos propios
#Crear y utilizar módulos personalizados
#Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el módulo. Por ejemplo, creamos un archivo (en el mismo directorio donde estamos ejecutando Python) llamado mi_modulo.py con el siguiente contenido:

#mi_modulo.py
'''def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b
'''
#Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py en otro archivo Python.


'''import mi_modulo

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8'''

#En este ejemplo, se importa el módulo mi_modulo y se utilizan las funciones saludar() y calcular_suma() definidas en él.

#Organización del código en módulos
#A medida que nuestros programas crecen en tamaño y complejidad, es una buena práctica organizar nuestro código en módulos separados según su funcionalidad. Esto nos permite conservar un código más legible, agrupado en módulos y fácil de mantener.
#Por ejemplo, podemos tener un módulo operaciones.py que contenga funciones relacionadas con operaciones matemáticas, y otro módulo utilidades.py que contenga funciones de uso general.
'''
# operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)

def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")
'''
#Luego, podemos importar y utilizar estas funciones en nuestro programa principal.


'''import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")
'''

#Paquetes

#Crear y utilizar paquetes
#Para crear un paquete, creamos un directorio con el nombre deseado y agregamos un archivo especial llamado __init__.py dentro del directorio. Este archivo puede estar vacío o contener código de inicialización del paquete.

#Por ejemplo, creamos un directorio llamado mi_paquete con la siguiente estructura:

'''mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py'''
#Luego, podemos importar y utilizar los módulos del paquete en nuestro programa.

'''from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2()'''
#En este ejemplo, se importan los módulos modulo1 y modulo2 del paquete mi_paquete y se utilizan las funciones definidas en ellos.
#La importación y creación de módulos y paquetes en Python nos permite organizar y reutilizar nuestro código de manera eficiente. Al modularizar nuestro código, podemos mantener un código más legible, estructurado y fácil de mantener.
#Recuerda explorar la biblioteca estándar de Python y aprovechar los módulos existentes, que pueden facilitarte muchas tareas comunes. Además, no dudes en crear tus propios módulos y paquetes para organizar y reutilizar tu código de manera efectiva.



'''x = 5
y = "3"
z = x + int(y)
print(z)'''