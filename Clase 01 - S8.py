from os import system
if system("clear") != 0: system("cls")

'''numeros = [1,2,3,4]
for x in numeros:
    print('Hola') #Se repetira 4 veces hola, porque 4 elementos hay en números
    
palabra = 'Aulas'
for z in palabra:
    print('Hola') #Se repetira 5 veces porque hay 5 elementos (letras) en palabra
    
días = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
for y in días:
    print(y) #Repetira cada elemento de la lista
for m in días[2]:
    print(m) #Dará cada elemento (letra) de miércoles 
for p in días:
    print(p[:2])''' #Imprime las primeras dos letras de cada elemento de días
 
 # FUNCIÓN RANGE
 #Permite crear secuencias
'''for i in range(10):   #El 'i' es el nombre que yo le asigno a cada uno de los iterables(elementos)
    print(i)'''    # Me da los números de 0 al 9, porque no toma en cuenta el 10.
    
'''personas = ['Ana','Luis','Juan']
for p in personas:
    for l in p:
        print(l) # Ingresar a los elementos de los elementos de 'personas'''
        
'''Valores = [[1,2,6],
           [2,7,4],
           [6,5,9],
           [1,10,20]]
mayores = []
númeromínimo = int(input())
for n in Valores:
    for m in n:
        if m > númeromínimo:
            mayores.append(m)  #Para ingresar los valores en la variable mayores
print(mayores)'''

# WHILE

'''inicio = 0
maximo = 5

while inicio < maximo:
    print('Hola')
    inicio = inicio + 1'''
    
'''presupuesto = 1000
gasto = 0
while gasto <= presupuesto:
    compra = float(input())
    gasto += compra #+= es lo mismo que decir gasto + compra
gasto -= compra
print(gasto)'''

estado = 'Conectado'
while estado == 'Conectado':
    print('Hola')
    estado = input('Digite su estado: ')


        
    
    