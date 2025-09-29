'''def frase(nombre, apellido, profesion):
    return f'Hola {nombre} {apellido}, tu profesion es {profesion}'''

#frase_resultado = frase('Nelson', 'Quillay', 'mecanico') #son parametros posicionales.
#frase_resultado = frase(profesion= 'mecanico', nombre= 'Nelson', apellido= 'Quillay') Esto se llama forzar argumento 'keyword arguments'

def frase(nombre, apellido, profesion = 'electricista'): #por defecto la profesion es electricista, es un parametro opcional
    return f'Hola {nombre} {apellido}, tu profesion es {profesion}'

frase_resultado = frase('Nelson', 'Quillay', 'mecanico')

print(frase_resultado)

