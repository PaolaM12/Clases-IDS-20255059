from os import system
if system("clear") != 0: system("cls")
# funciones
'''print('hola mundo')''' # los parentesis se llaman parámetros y lo de adentro se llama argumentos

# Hay que crear modulos que contendrán funciones
#Una función tiene 2 tiempos, una definición y una llamada
#Vamos a definir una función

def mi_funcion():
    '''Esta función imprime un saludo'''
    print('Hola mundo')
    print('amigo usuario')
    print('gracias por usar nuestro sistema')
    
# ahora podemos utilizarla y llamar la función

mi_funcion()
mi_funcion()
mi_funcion()
mi_funcion() # Una función para que funcione tiene que llevar paréntesis

#Vamos a recibir información desde afuera de la función con input
def capturar_nombre():
    '''Esta función recibe valores por medio de input'''
    nombre_input = input('Escriba su nombre: ')
    apellido_input = input('Escriba su apellido: ')
    nombre_completo = nombre_input + ' ' + apellido_input
    print(nombre_completo)
    
# por medio de argumentos
def capturar_usuario(nombre, edad):
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f'El usuario se llama {nombre_usuario} y tiene {edad_usuario} años'
    print(texto)

# Llamando la función capturar_nombre()
capturar_usuario(input('Ingrese su nombre: '), input('Edad: '))

# Función que devuelve un valor
def calculo_impuesto(ventas):
    '''Esta función calcula el valor del impuesto'''
    if ventas <500:
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.24
    return tasa_impuesto

ventas = 1000
print(f'''El valor de la venta fue de {ventas:,.2f},
      la tasa de impuesto es {calculo_impuesto(ventas)} y el monto por tanto es ${calculo_impuesto(ventas)*ventas:,.2f}''')