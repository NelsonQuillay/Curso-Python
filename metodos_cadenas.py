cadena1 = 'hola,como,estas,bobo'
cadena2 = 'hi'

mayusc = cadena1.upper() #convierte todo a mayuscula
minusc = cadena1.lower() #convierte todo a minuscula
primera_letra_mayusc = cadena1.capitalize() # convierte todo en minuscula y luego a mayuscula la primera letra
busqueda_find = cadena1.find('hola') #busca el valor que pasamos entre () y devuelve la posicion en la cadena, si no hay coicidencia devuelve -1
#busqueda_index = cadena1.index('hola') #busca el valor que pasamos entre () y devuelve la posicion en la cadena, si no hay coicidencia devuelve una excepcion
es_numerico = cadena1.isnumeric() #si es numerico devuelve true, caso contrario false
es_alfanumerico = cadena1.isalpha() #si es alfanumerico devuelve treu, caso contrario false
contar_coincidencias = cadena1.count('a') #busca el valor que pasamos entre () y nos devuelve la cantidad de veces que coincida
contar_caracteres = len(cadena1) #!LEN NO ES UN METODO, ES UN FUNCION. Devuelve cantidad de caracteres que tiene una cadena.
empieza_con = cadena1.startswith('hH') #Verificmos si una cadena empieza con el valor que pasamos entre (), si coincide devueolve true.
termina_con = cadena1.endswith('la ') #Verificmos si una cadena termina con el valor que pasamos entre (), si coincide devueolve true.
cadena_nueva = cadena1.replace('ho','LOOOOO') #si el valor 1 se encuentra en la cadena original 'cadena1', la reemplaza por el valor 2.
cadena_separada = cadena1.split(',') #separa cadena con el valor que le pasamos entre ()

print(cadena_separada)