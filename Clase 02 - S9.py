from os import system
if system("clear") != 0: system("cls")


usuarios = ['Ana','Carlos','Luis']
for i, usuario in enumerate(usuarios):  # la función enumerate enumera desde 0 hasta que yo indique lo contrario
    print(f'{i} {usuario}')
    
usuarios = ['Ana','Carlos','Luis','Lorenzo','Juan','Luis','Paola','Mónica','Mario','Ale']
for i, usuario, in enumerate (usuarios, start=1):  # Si le pongo start = 1, empezará desde 1
    print(f'{i} {usuario}')
    
usuarios = ['Ana','Carlos','Luis','Lorenzo','Juan','Luis','Paola','Mónica','Mario','Ale']
edades = [20,19,21,30,40,50,63,98,60,20,40,10]
frutas = ['mango','pera','manzana','melocotón','sandia','piña','manzana','pera','fresa','piña']
for usuario, edades, frutas in zip (usuarios, edades, frutas):  # zip es para unir listas
    print(f'{usuario} {edades} {frutas}')     # Para que funcione bien tiene que estar emparejadas todas las listas

    
    