from os import system
if system("clear") != 0: system("cls")

# Vamos a jugar un juego
'''aprobación = True
while aprobación:
    elección = input('Quieres seguir jugando? (YES/NO):')
    if elección.lower() == 'no':
        aprobación = False    #si pusiera cualquier otro valor que no sea NO me lo seguirá tomando como yes, en cambio si le pongo NO en mayuscula como tal si va a detenerse. Por ello, le pongo.lower
    elif elección.lower() == 'yes':
        print('Me alegra que sigas jugando')
    else:
        print('La opción elegida no es válida.')'''
    
# Una aplicación para registrar alumnos
'''alumnos = [] # lista vacía que iré alimentando
alumnoarecibir = input()
alumnos.append(alumnoarecibir) #para meterlos en la lista
alumnoarecibir = input()
alumnos.append(alumnoarecibir)
alumnoarecibir = input()
alumnos.append(alumnoarecibir)
print(alumnos)'''              # esta forma puede ser un tanto larga.

#segunda forma
'''alumnos = []
for a in range(int(input())):
    alumno = input()
    alumnos.append(alumno)
print(alumnos)'''

# Sistema de gestión de alumnos
menu_iniciado = True
alumnos = []         #if len(alumnos) == 10 print('No hay')
while menu_iniciado:
    opción = int(input('1. Agregar, 2. Consultar, 3. Modificar, 4. Borrar, 5. Salir: '))
    if opción == 5:
        menu_iniciado = False
    elif opción == 1:
        alumnos.append(input('Digite el nombre del alumno: '))
        print(alumnos)
    elif opción == 2:
        for a in alumnos:   # Por cada a imprimira cada alumno en listas separadas
            print(a)
    elif opción == 3:
        indice = int(input('Digite el número del alumno (1-3) '))
        nuevo = input('Digite el nombre nuevo: ')
        alumnos[indice-1] = nuevo    # le pongo -1 porque los indices son de 0 en adelante
    elif opción == 4:
        indice = int(input('Digite el número del alumno (1-3) a popear: '))  # borro en un orden específico y lo guardo con pop
        alumno_borrado = alumnos.pop(indice-1)
        print(f'Hemos borrado a {alumno_borrado}')
    else:
        print('Esa opción no es válida')
        
print('Gracias por usar nuestro sistema')



