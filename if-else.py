'''edad = 17

if edad >= 18:
    print('Mayor de edad')

else: 
    print('No podes pasar')'''

'''contraseña_almacenada = 'nelson123'
contraseña_ingresada = 'nelson23'

if contraseña_almacenada == contraseña_ingresada:
    print('se inicio correctamente sesion')

else:
    print('contraseña incorrecta, intente de nuevo')'''

#if anidados y else if (elif)

ingreso_mensual = 81000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print('estas en bancarota')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('estas joya en el mes')
    else:
        print('estas en el horno en este mes')

elif ingreso_mensual > 1000:
    print ('estas bien')

elif ingreso_mensual > 500:
    print ('la piloteas')

else:
    print('sos pobre')