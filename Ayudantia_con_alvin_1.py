from os import system
if system("clear") != 0: system("cls")

#Ejercicio 1
"""
correo = input("ingrese su correo electronico \n :::")

##busco evaluar true or false
##debe de contener exactamente un arroba


#Count dice que quiero que me cuente cuantos caracteres hay que sean iguales a la casilla adentro de los parentesis
#condicion1 = correo.count("@")==1
#posicion_arroba = correo.index("@")
#Index me dice en que posicion esta el arroba 
condicion1 = correo.count("@")==1
posicion_arroba = correo.index("@")
condicion2= correo.index("@") >= 3 and (len(correo) - posicion_arroba) > 3
condicion3 = correo.count(".") >= 1
condicion4 = correo.count(" ")==0
condicion5 = correo[0] != "." and correo[-1] != "."

print(condicion1, condicion2, condicion3, condicion4, condicion5)
"""

#Ejercicio 2
"""
cadena = input("")
print(cadena.lower().count("z"))
"""
"""
X = int(input()) #3
A = input() #Lapiz
B = input() #mochila

print(A[:X:] + B[-X:])
"""

#Ejercciio 3
"""
#X = int(input()) #3
A = input() #Lapiz
#B = input() #mochila

print(A[::-1])
"""

#Ejercicio 4
"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print((n1*n2)-(n3*n4))
"""

#Ejercicio 5
"""
A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())

lista = [A, B, C, D, E, F]
print(lista)

print(f"Maximo: {max(lista):.2f}")
print(f"Minimo: {min(lista):.2f}")
print(f"Diferencia: {(max(lista) - min(lista)):.2f}")
print(f"Suma: {sum(lista):.2f}")
print(f"Promedio: {(sum(lista) / len(lista)):.2f}")
"""

#Ejercicio 6
"""
E1 = int(input())
E2 = int(input())
E3 = int(input())
E4 = int(input())
E5 = int(input())
D1 = float(input())
D2 = float(input())
D3 = float(input())
D4 = float(input())
D5 = float(input())

print(int((E1*D1)+(E2*D2)+(E3*D3)+(E4*D4)+(E5*D5)))
"""

#Ejercicio 7
""" 
nombre = (input(""))
apellido = (input(""))

nick = (nombre[:5] + apellido [0]).lower()
pin = (len(nombre) * 1000 + len(apellido)) % 10000
id_completo = (f"C3-{nick}-{pin}")

print(f"Nick: {nick}")
print(f"Pin: {pin}")
print(f"ID: {id_completo}")
"""

#Ejercicio 8
"""
fecha = input()
print(fecha[6:] + "/" + fecha[3:5] + "/" + fecha[:2])
"""

#Ejercicio 9
"""
plato_principal = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
complementos = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")

num_plato = int(input("")) - 1
num_complemento = int(input("")) - 1

plato = plato_principal[num_plato]
complemento = complementos[num_complemento]

print(f"El pedido de alvin es: {plato} con {complemento}")
"""

#Ejercicio 10
"""
N = int(input(""))

suma = N * (N + 1) / 2

print(int(suma))
"""

