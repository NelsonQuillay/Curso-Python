#duracion de los cursos
otros_cursos_max = 7
otros_cursos_min = 2.5
otros_cursos_promedio = 4
dalto_curso = 1.5


#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de duracion 
direfencia_con_min = 100 - dalto_curso / otros_cursos_min *100
direfencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
direfencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio *100

#calcular el porcentaje de tiempo vacio remocido
tiempo_vacio_promedio = 100 - otros_cursos_promedio / crudo_promedio *100
tiempo_vacio_dalto = 100 - dalto_curso *1000 // crudo_dalto /10

print('-------------------------------------------------------------------------')
#mostrando la diferencia de diracion (ejercicio A)
print('el curso de dalto dura:')
print(f' - un {direfencia_con_min}% menos que el curso mas rapido')
print(f' - un {direfencia_con_max}% menos que el curso mas lento')
print(f' - un {direfencia_con_promedio}% menos que el promedio de los cursos')

print('-------------------------------------------------------------------------')
#mostrando la cantidad de espacio vacio que se remueve (ejercicio B)
print(f'un curso promedio elimina {tiempo_vacio_promedio}% de tiempo vacio')
print(f'el curso de dalto elimina {tiempo_vacio_dalto}% de tiempo vacio')

print('-------------------------------------------------------------------------')
#mostrando diferencia si los cursos duraran 10 horas 
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otro curso promedio')
print(f'ver 10 horas de otro cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de curso dalto')
