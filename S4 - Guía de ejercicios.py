#SECCIÓN 4: f-strings y formato de salida
#Ejercicio 1
nombre = 'Ana'
producto = 'Laptop'
precio = '$1200.00'
print(f'Hola {nombre}, el producto {producto} cuesta {precio}.')
#Ejercicio 2
nombre = input('Ingresa tu nombre: ')
país = input('Ingresa de done vienes: ')
print(f'Hola {nombre} de {país}, ¡bienvenido!')
#Ejercicio 3
nombre = input('¿Cuál es tu nombre? ')
edad = input('¿Cuál es tu edad? ')
ciudad = input('¿Cuál es tu ciudad de procedencia? ')
print(f'Resumen de información')
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'Ciudad: {ciudad}')
#Ejercicio 4
base = float(input('Indica la base del rectangulo: '))
altura = float(input('Indica la altura del rectangulo: '))
print(f'El area del rectangulo es {base*altura:.2f}')
#Ejercicio 5
producto = 'pan'
precio = 1.50
cantidad = 4
total = 6.00
print(f'Producto: {producto}, Precio {precio:.2f}, Cantidad: {cantidad}, Total: {precio*cantidad:.2f}')


