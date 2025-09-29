#crear una funcion simple

'''def saludar():
    print('hola Neldon en que te puedo ayudar?')

#ejecutando la funcion simple
saludar()'''

#creando una funcion que tenga parametros
'''def saludar(nombre):
    print(f'Hola {nombre} en que te puedo ayudar?')

saludar('Pepe')'''

'''def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif (sexo == 'hombre'):
        adjetivo = 'capo' 
    else:
        adjetivo = 'amor'
    print(f'Hola {nombre}, mi {adjetivo} en que te puedo ayudar?')

saludar('Nelson', 'HOMBRE') #Hola Nelson, mi capo en que te puedo ayudar?'''

#Crear una funcion que nos devuelve valores
def crear_contraseña_random(num):
    chars = 'lmnopqrstu'
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 3
    contraseña = f'{chars[c1]}{num*2}{chars[c2]}{num*3}{chars[c3]}'
    #print(contraseña)
    return contraseña, num # el return para guardar los valores y luego poder usarlos

password = crear_contraseña_random(5)
frase = f'tu nueva contraseña es: {password}'
print(frase)