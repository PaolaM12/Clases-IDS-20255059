# A. Positivo o negativo
'''número = int(input())
if número > 0:
    print('Positivo')
elif número < 0:
    print('Negativo')'''
    
# B. Anterior y posterior
'''S = int(input())
if S % 2 == 0:
    print(S+2)
else:
    print(S+1)
if S % 2 == 0:
    print(S-1)
else:
    print(S-2)'''
    
# C. Promedio
'''nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
nota5 = float(input())
nota6 = float(input())

promedio = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6) / 6

if promedio > 9.5:
    print('Gana Premio :)')
else:
    print('No Gana Premio :(')'''
    
# D. Escoger números 7 y 5
'''N = int(input())
numeros7 = 0
numeros5 = 0
for i in range(N):
    numero = int(input())
    if numero == 7:
        numeros7= numeros7 + 1
    elif numero == 5:
        numeros5 = numeros5 + 1
print(numeros7, numeros5)'''
    


# E. Los combos de David
N = int(input())
Pa, Pb, Pc= map(int,input().split())
for i in range(N):
    combo = input()
    total = 0
    for daño in combo:
        if daño == 'A':
            total += Pa
        elif daño == 'B':
            total += Pb
        elif daño == 'C':
            total += Pc
    print(total)
        
    
    
# F. Bodoque el enamorado
'''cantidadamores = int(input())
for cantidad in range(cantidadamores):
    amores = input()
    if len(amores)<=6:
        print('No vale la pena')
    elif len(amores)>= 8:
        print('Si aguanto otro desarrollo de personaje')
    elif len(amores)>6 and len(amores)<8:
        print('Dios no creo aguantar esta vez')'''


# G. P2: Número mayor
'''numero1, numero2 = map(int,input().split())
if numero1 > numero2:
    print(numero1)
elif numero2 > numero1:
    print(numero2)'''
    
# H. Entrada al cine
'''fila = int(input())
personas = 0
i = 0
while i < fila:
    edad = int(input())
    if edad >= 15:
        personas += 1
    i += 1
print(personas)'''

# I. Ola Ivan
'''estado = input()
while estado == 'conectado':
    print('Ola Ivan')
    estado = input('')
print('Ol..')

estado = input()
if estado == 'conectado':
    print('Ola Ivan')
elif estado == 'desconectado':
    print('Ol..')'''
    
# E. Software Libre
'''N = int(input())
for i in range(N):
    Pi = int(input())
    if Pi >= 3:
        print('Ok')
    else:
        print('No')'''



