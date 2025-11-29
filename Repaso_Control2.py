#Ejercicio 1
#Problema:Vas a capturar la cantidad de artículos producidos en abril, mayo y junio.
# Los costos unitarios de producción son:Abril: $1.45
# Mayo: $1.32 Junio: $1.27
# Muestra en pantalla el costo total de producción de los tres meses.

ABRIL = 1.45
MAYO = 1.35
JUNIO = 1.27
cantidad_abril = int(input(''))
cantidad_mayo = int(input(''))
cantidad_junio = int(input(''))
costo_total = ((ABRIL*cantidad_abril)+(MAYO*cantidad_mayo)+(JUNIO*cantidad_junio))
print(f'{costo_total:.2f}')

#Ejercicio 2
#Crea una lista con los cinco días laborales de la semana (lunes a viernes).
# Pide al usuario que ingrese la cantidad de productos vendidos cada día, y después de cada entrada muestra:
# “El día MARTES se vendieron 250 productos”
# Al final, muestra la suma total de productos vendidos en la semana.

dias = ['LUNES','MARTES','MIERCOLES','JUEVES', 'VIERNES']
cantlunes = int(input(''))
print(f'El día {dias[0]} se vendieron {cantlunes} productos')
cantmartes = int(input(''))
print(f'El día {dias[1]} se vendieron {cantmartes} productos')
cantmiercoles = int(input(''))
print(f'El día {dias[2]} se vendieron {cantmiercoles} productos')
cantjueves = int(input(''))
print(f'El día {dias[3]} se vendieron {cantjueves} productos')
cantviernes = int(input(''))
print(f'El día {dias[4]} se vendieron {cantviernes} productos')

print(cantlunes+cantmartes+cantmiercoles+cantjueves+cantviernes)

#Ejercicio 3
#Tienes 6 niños que darán su fruta favorita.
# Crea una lista inicial llamada frutas con los valores [1, 2, 3, 4, 5, 6].
# Pide 6 veces al usuario que ingrese una fruta y reemplaza el número por la fruta ingresada.
# Después de cada ingreso muestra la lista actualizada.

frutas = ['1','2','3','4','5','6']
niño = int(input(''))
fruta_favorita = input('')
frutas[niño] = fruta_favorita
print(frutas)
niño = int(input(''))
fruta_favorita = input('')
frutas[niño] = fruta_favorita
print(frutas)
niño = int(input(''))
fruta_favorita = input('')
frutas[niño] = fruta_favorita
print(frutas)
niño = int(input(''))
fruta_favorita = input('')
frutas[niño] = fruta_favorita
print(frutas)
niño = int(input(''))
fruta_favorita = input('')
frutas[niño] = fruta_favorita
print(frutas)
niño = int(input(''))
fruta_favorita = input('')
frutas[niño] = fruta_favorita
print(frutas)

#Ejercicio 4
#Crea una tupla con los nombres de 7 estudiantes en el orden en que entraron al salón.
# Luego pide al usuario que ingrese un número del 1 al 7 y muestra:
# “El alumno que ingresó como número X es NOMBRE”.

tupla = ('Ana','Juan','Pedro','Sofía','Roberto','Jaime','Paola')
número = int(input(''))
print(f'El alumno que ingresó como número {número} es {tupla[número-1]}')
número = int(input(''))
print(f'El alumno que ingresó como número {número} es {tupla[número-1]}')
número = int(input(''))
print(f'El alumno que ingresó como número {número} es {tupla[número-1]}')
número = int(input(''))
print(f'El alumno que ingresó como número {número} es {tupla[número-1]}')
número = int(input(''))
print(f'El alumno que ingresó como número {número} es {tupla[número-1]}')
número = int(input(''))
print(f'El alumno que ingresó como número {número} es {tupla[número-1]}')
número = int(input(''))
print(f'El alumno que ingresó como número {número} es {tupla[número-1]}')

#Ejercicio 5
#Pide al usuario que ingrese su salario (puede incluir $).
# Valida por separado:
# a) Que haya exactamente un símbolo $.
# b) Que el símbolo $ esté al inicio de la cadena.

salario = input('')
print(salario[0]=='$')
print(salario.count('$')==1)

#Ejercicio 6
#Problema:Pide al usuario que ingrese nombre y apellido.
# Genera dos propuestas de correo electrónico para la empresa TECNOX.
# Ejemplo con entrada: Maria GonzAlez
# Salida esperada:
# Propuesta 1: maria.gonzalez@TECNOX.com
# Propuesta 2: mgonzalez@TECNOX.com

nombre = input('')
apellido = input ('')
print(f'{nombre.lower()}.{apellido.lower()}@TECNOX.com')
print(f'{nombre.lower()[0]}{apellido.lower()}@TECNOX.com')

#Ejercicio 7
#Problema: Tienes un texto encriptado: aqqwerztyuio
# La contraseña real está escondida tomando una letra sí y dos no, empezando desde el primer carácter.
# Extrae y muestra la contraseña descifrada.

texto = 'aqqwerztyuio'
print(texto[::3])




