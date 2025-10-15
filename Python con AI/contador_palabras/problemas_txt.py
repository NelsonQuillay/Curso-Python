#2 lista, una con nombres y la otra con apellidos
nombres = ['nelson', 'melina', 'maximo', 'alvaro', 'mario']
apellidos = ['quillay', 'quiroga', 'perez', 'orozco', 'lopez']

#registrar esta informacion en un txt de forma rapida
with open("archivo_problemas\\nombres_y_apellidos.txt", "w") as archivo:
    archivo.writelines("los datos son: \n\n")
    '''
    for n,a in zip(nombres, apellidos):
        archivo.writelines(f'Nombre: {n}\nApellido: {a}\n-------------\n')
    '''
    #para hacerlo en una sola linea tiene que estar dentro de una lista/array
    [archivo.writelines(f'Nombre: {n}\nApellido: {a}\n-------------\n') for n,a in zip(nombres, apellidos)]