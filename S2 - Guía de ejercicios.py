#SECCIÓN 2: input() y conversión de tipos (casting)
#Ejercicio 1
nombre = input('¿Cuál es tu nombre?')
print(f'Hola, {nombre}. ¡Espero estes bien!')
#Ejercicio 2
edad = int(input('¿Cuál es tu edad?'))
print(f'El doble de tu edad es {edad * 2}')
#Ejercicio 3
numero1 = int(input('Dime un número entero: '))
numero2 = int(input('Dime otro número entero: '))
print(f'La suma de tus números elegidos es {numero1+numero2}')
#Ejercicio 4
numerodecimal = float(input('Dime un número decimal: '))
print(f'La mitad de tu número es {numerodecimal/2}')
#Ejercicio 5
añonacimiento= int(input('¿Cuál es tu año de nacimiento?'))
print(f'Tu edad actual es {2025-añonacimiento}')
#Ejercicio 6
precio = float(input('¿Cuál es el precio? $'))
unidades = int(input('¿Cuántas cantidades llevas? '))
totaldepago = precio*unidades
print(f'Tu total a pagar es ${totaldepago}')
#Ejercicio 7
númeroentero = int(input('Dame un número entero: '))
print(f'El cuadrado de tu número es {númeroentero**2}')
#Ejercicio 8
num1 = float(input('Dame un número: '))
num2 = float(input('Dame otro número: '))
print(f'El promedio de los dos números es {num1 + num2 /2}')
#Ejercicio 9
nombre_usuario = input('Hola, escribe tu nombre compelto: ')
edad_usuario = int(input('Ahora indica tu edad: '))
print(f'Hola {nombre_usuario}, espero te encuentres bien. Tienes {edad_usuario} años.')

