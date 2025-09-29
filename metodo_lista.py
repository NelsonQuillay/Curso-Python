# METODO DE LISTA = METODO DE ARREGLOS O ARRAY

lista = list([10, 37, 30, True, False]) #crando una lista con list()
cantidad_elementos = len(lista) #devuelve la cantidad de elementos de una lista
lista.append(True) #agregamos un elemento al final de la lista
lista.insert(1, False) #agrega un elemento a la lista en un indice especifico
lista.extend([11,False]) # agregando varios elementos a la lista al final
lista.pop(2) #eliminando un elemento a la lista por su indice, (-1) se elimina el ultimo elemento a la lista (-2) el anteultimo
lista.remove(30) #buscar elemento y si lo encuentra se elimina y larga error si no hay coicidencia
lista.sort() #se ordena la lista
lista.sort(reverse=True) #reverse lo ordena en reversa
elemento_encontrado = lista.index(True)
#lista.clear() #elimienado todos los elementoas de la lista
print(elemento_encontrado)