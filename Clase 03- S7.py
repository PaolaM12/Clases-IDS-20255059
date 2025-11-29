from os import system
if system("clear") != 0: system("cls")


'''nota = float(input('Indique la nota:'))
if nota >= 6:
    print('Aprobado')  
else:
    print('No aprobaste')'''
    
'''nota = float(input('Indique la nota:'))
if nota == 10:
    print('E')
else:
    if nota > 7:
        print('MB')
    else:
        if nota > 5:
            print('B')
        else:
            if nota > 3:
                print('R')
            else:
                print('M')'''
                
# IMPUESTOS
'''valor_impuesto = float(input())
local_o_importado = input()
impuesto = 0 
if local_o_importado.lower() == 'local':
    if valor_impuesto > 500:
            impuesto = 0.1
    else:
        if valor_impuesto > 200:
            impuesto = 0.08
        else:
            if valor_impuesto > 50:
                impuesto = 0.06
            else:
                impuesto = 0
elif local_o_importado.lower()=='importado':
    if valor_impuesto > 500:
        impuesto: 0.14
    else:
        if valor_impuesto > 200:
            impuesto = 0.12
        else:
            if valor_impuesto > 50:
                impuesto = 0.1
            else:
                impuesto = 0
else:
    print('Ese tipo no es válido')
    
print(f'El impuesto a pagar de tipo {local_o_importado} por venta de {valor_impuesto:,.2f}')
print(f'es de {valor_impuesto*impuesto:,.2f}')'''
    
# CON ELIF
'''valor_impuesto = float(input())
local_o_importado = input()
impuesto = 0 
if local_o_importado.lower() == 'local':
    if valor_impuesto > 500:
            impuesto = 0.1
        else:
            if valor_impuesto > 200:
                impuesto = 0.08
            else:
                if valor_impuesto > 50:
                    impuesto = 0.06
                else:
                    impuesto = 0
elif local_o_importado.lower():'importado':
    if valor_impuesto > 500:
        impuesto: 0.14
    else:
        if valor_impuesto > 200:
            impuesto = 0.12
        else:
            if valor_impuesto > 50:
                impuesto = 0.1
            else:
                impuesto = 0
else:
    print('Ese tipo no es válido')'''

# FOR
nombre = ['Ana','Luis','Jose','María','Paola','Alvin','Rolo'] # nombres es iterable y 1,2,3 son iteradores
nombre_a_buscar = input()
for nombresito in nombre:   # yo pongo el nombre de 'numerito' esto hace que por cada 'numerito' se imprima un 'hola'
    print('Hola')
    
for nombresito in nombre:
    print(nombresito)    # Si digo que imprima 'numerito' va a imprimir lo que está dentro de la lista
    
for nombresito in nombre:
    if nombresito == 2:          # Busca en todos los iteradores para ver si está lo que yo le indico, hasta que lo encuentre
        print('Ya lo encontre')
    else:
        print('Aquí no está')