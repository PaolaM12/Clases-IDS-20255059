def describir_mascota(tipo_animal: str, nombre_mascota: str):   # Si por defecto yo quiero que sea perro le pongo str = 'perro')
    '''Esta función describe una mascota'''
    print(f'Mi mascota se llama {nombre_mascota} y es de tipo {tipo_animal}')
    
#describir_mascota('perro','beba')  # Si el usuario pusiera solo un valor, por defecto el sistema diría que es un perro
#describir_mascota(nombre_mascota='gato',tipo_animal='mich') # Con eso yo decido el orden

def registro_usuarios(nombre, apellido, inicial='', edad=0):  # Si no hay inicial para que no de error se puede poner = ''
    '''construir un nombre a partir de sus componentes'''
    if edad:
        nombre_completo = f'{nombre} {inicial} {apellido} {edad}'
    else:
        nombre_completo = f'{nombre} {inicial} {apellido}'  # Si hay edad se muestra la opción, si no hay se toma la segunda
    return nombre_completo
# print(registro_usuarios('Daniel','Ríos','A',50))

# Definimos una función que es usada por una lista

def saludar_usuarios(nombres):
    '''Saludará usuario'''
    for nombre in nombres:
        print(f'Hola, {nombre}')
usuarios = ['Ana','Luis','Sebas']
#saludar_usuarios(usuarios)

# Vamos a proceder a atender pedidos de pizza
def ordenar_pizza(ingrediente):
    '''Vamos a imprimir su orden'''
    print(f'Usted ha ordenado una pizza de {ingrediente}')
#ordenar_pizza(input(''))

def ordenar_pizza(size, *ingrediente): # El asterisco dice que es una lista, es un parametro de tipo args y va al final de todos los parámetros
    '''Vamos a imprimir su orden'''
    print(f'Usted ha ordenado una pizza {size} de:')
    for i in ingrediente:
        print(f'{i}')
ordenar_pizza('grande','jamon','queso')