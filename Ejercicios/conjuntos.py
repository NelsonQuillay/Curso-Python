#creando un conjunto con set()
conjunto = set(['datos1', 'datos2'])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset (['datos3', 'datos4']) #conjunto congelado
conjunto2 = {conjunto1, 'datos5'}

print(conjunto2)


#teorias de conjuntos

conjunto3 = {1, 3, 5, 7}
conjunto4 = {1, 3, 7}

#verificando si es un subconjunto
resultado = conjunto4.issubset(conjunto3)# true conjunto4 es un subconjunto de conjunto3
resultado1 = conjunto3.issubset(conjunto4)# false

#otra forma de verificar si es un subconjunto
resultado2 = conjunto4 <= conjunto3 # true
resultado3 = conjunto3 <= conjunto4 # false 

resultado4 = conjunto4.issuperset(conjunto3)# false conjunto4 es un subconjunto de conjunto3
resultado5 = conjunto3.issuperset(conjunto4)# true

#otra forma de verificar si es un subconjunto
resultado6 = conjunto4 > conjunto3 # false
resultado7 = conjunto3 > conjunto4 # true


conjunto5 = {1, 3, 5, 7}
conjunto6 = {2, 4, 8}

#verificar si NO hay algun numero en comun
resultado8 = conjunto6.isdisjoint(conjunto5) #True si hay algun resultado en comun

print(resultado8)