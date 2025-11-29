# EJERCICIO 1
# Después del desastre con el generador automático de correos y el intento de realizar un programa para encontrar los correos inválidos, la ESEN se dio cuenta de que el programa era demasiado simple y permitió que muchos correos incorrectos pasaran las pruebas.
# Por esta razón, la ESEN quiere desarrollar un nuevo programa, más complejo y sofisticado, que les ayude a validar de mejor forma los correos y así tenerlos listos para sus alumnos de nuevo ingreso 2026.
# Te han asignado la misión de crear este nuevo programa. Tu programa debe recibir un correo a validar e imprimir un mensaje que indique si es válido o inválido (True/False). Para que un correo se considere válido, debe cumplir las siguientes condiciones:
# El correo contiene exactamente un @
# Antes y después del @ debe haber al menos 3 caracteres
# El correo debe contener al menos un punto
# El correo no puede contener espacios
# El correo no puede iniciar ni terminar con un punto

# Restricciones
# Todos los correos tendrán mínimo un arroba, aunque pueden tener varios.
# Entrada
# Una sola línea con un correo electrónico a validar.
# Salida
# Una sola línea con un mensaje que indique si el correo cumple todas las condiciones (True) o no (False).

'''correo = input()
cond1 = correo.count('@')==1
cond2 = correo.index('@')>=3 and (len(correo) - correo.index('@'))>3
cond3 = correo.count('.')>=1
cond4 = correo.count(' ')==0
cond5 = correo[0]!='.'and correo[-1]!='.'

print(cond1 and cond2 and cond3 and cond4 and cond5)'''

# EJERCICIO 2
#Enunciado
# Un dragón duerme sobre una cadena de letras. Para que no despierte, debes contar cuántas veces aparece la letra z en la cadena.
# Entrada:
# Una cadena de hasta 100 caracteres en minúsculas
# Salida:
# Un número entero con la cantidad de letras z.

'''cadena = input()
print(cadena.lower().count('z'))'''

# EJERCICIO 3
# ¡Otra vez! En la ESEN, estamos experimentando demasiados problemas con las contraseñas. Esta vez, la víctima es el pobre OOF.
# Al igual que con la contraseña de Alvin, Issem es el malandro que ha hackeado y encriptado la contraseña de Steam de OOF. No obstante, esta vez no se llegó a un acuerdo con el Señor Oscuro, por lo que podemos esperar que la recuperación de la contraseña no será tan sencilla como la vez pasada.
# Afortunadamente, con la ayuda del coco de Rober Polanski, hemos sido capaces de descifrar la forma de recuperar la contraseña, siendo así:
# Polanski encontró 2 palabras escondidas (A y B).
# La primera parte de la contraseña, son los primeros caracteres de A, donde representa el tamaño de la cadena 
# La segunda parte de la contraseña, son los últimos caracteres de B, donde representa el tamaño de la cadena 
# ¿Puedes ayudar a que OOF recupere su cuenta de Steam?
# Entrada
# La primera línea contiene un único entero X, los caracteres que tienes que tomar en cuenta. La segunda línea presenta una cadena de caracteres A. La última línea contiene una cadena de caracteres B.
# Salida
# Imprime una única cadena de caracteres, la contraseña recuperada
# Restricciones
# El tamaño de A y B siempre será a lo sumo 100 caracteres X siempre será un divisor del tamaño de A y B, aunque dichas cadenas no tengan el mismo tamaño.

'''número = int(input())
cadenaA = input()
cadenaB = input()

print(cadenaAA[0:(len(cadenaAA)//número)] + cadenaB[-(len(cadenaB)//número):])'''

# EJERCICIO 4
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

print((num1*num2)+(num3*num4))



