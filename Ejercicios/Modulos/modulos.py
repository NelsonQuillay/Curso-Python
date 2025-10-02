import modulo_saludar

hola = modulo_saludar.saludar('Nelson')
print(hola)

#usando el operador as sirve para asignar otro nombre
import modulo_saludar as ms

hello = ms.saludar('Quillay')
print(hello)

#si solamente queremos importar una sola funcionar de un modelo
from modulo_saludar import saludar
'''from NuevaCarpeta.modulo_saludar import saludar
eso es para cuendo el modulo esta en otra carpeta'''


hi = saludar('Mario')
print(hi)

#si queremos importar mas de dos funciones pero no todas las del modulo
from modulo_saludar import saludar, saludar_ingles
#from modulo_saludar import saludar as saludar_español, saludar_ingles as saludar_en_otro_idioma '''usamos el operador as para renombrar'''

saludo = saludar('Melina')
#saludo = saludar_español('Melina')
saludo_ingles = saludar_ingles('Quiroga')
#saludo_ingles = saludar_en_otro_idioma('Quiroga')

print(saludo)
print(saludo_ingles)

from modulo_saludar import * # se utiliza * para importar todas las funciones que tiene el modulo pero se considera una mala practica

#para ver las propiedades y metodos  de el namespace
#print(dir(modulo_saludar))
