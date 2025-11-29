'''numero = int(input().strip())
cadena1 = input().strip()
cadena2 = input().strip()
parte1 = cadena1[:numero]
parte2 = cadena2[-numero:]
contrasena = parte1+parte2
print(contrasena)'''

'''X = int(input(""))
A = input("")
B = input("")
print(A[0:(len(A)//X)] + B[-(len(B)//X):])'''

'''num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

print((num1*num2)-(num3*num4))'''

'''nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())
nota6 = float(input())
lista = (nota1,nota2,nota3,nota4,nota5,nota6)

print(f'Maximo: {max(lista):.2f}')
print(f'Minimo: {min(lista):.2f}')
print(f'Diferencia: {max(lista)-min(lista):.2f} ')
print(f'Suma: {sum(lista):.2f}')
print(f'Promedio: {sum(lista)/len(lista):.2f}')'''

'''p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
p5 = int(input())
por1 = float(input())
por2 = float(input())
por3 = float(input())
por4 = float(input())
por5 = float(input())

print(int((p1*por1)+(p2*por2)+(p3*por3)+(p4*por4)+(p5*por5)))'''

nombre = input()
apellido = input()
nickk = (nombre[:5] + apellido[0]).lower()
pin = len(nombre) * 1000 + len(apellido) % 10000
ID_completo = (f'C3-{nickk}-{pin}') 
print(f'Nick: {nickk}')
print(f'Pin: {pin}')
print (f'ID: {ID_completo}')


'''F = input()
print(f'{F[6:10]}/{F[3:5]}/{F[:2]}')'''

'''Platos = ('Hamburguesa','Pizza','Tacos','Pupusas','Hotdog')
Complementos = ('Papas fritas','Alitas de pollo','Ensalada','Sopa','Lasaña')
p = int(input())
c = int(input())
print(f'El pedido de Alvin es: {Platos[p-1]} con {Complementos[c-1]}')'''

'''Entero = int(input())
suma = (Entero*(Entero+1))/2
print(int(suma))'''



