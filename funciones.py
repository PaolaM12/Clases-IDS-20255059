#Aquí van todas las funciones
def ordenar_pizza(size, *ingrediente): # El asterisco dice que es una lista, es un parametro de tipo args y va al final de todos los parámetros
    '''Vamos a imprimir su orden'''
    print(f'Usted ha ordenado una pizza {size} de:')
    for i in ingrediente:
        print(f'{i}')
        
def registro_profesores(nombre, apellido, **materias):
    '''Crear un registro de profesor, utilizando kwargs''' #kwargs es para crear diccionarios
    print(f'El profesor {nombre} {apellido} imparte las materias: ')
    for ciclo, materias in materias.items():
        print(f'-{ciclo}:{materias}')
        
def saludar_usuarios(nombres):
    '''Saludará usuario'''
    for nombre in nombres:
        print(f'Hola, {nombre}')

