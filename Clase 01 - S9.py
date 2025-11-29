from os import system
if system("clear") != 0: system("cls")

# Vamos a crear nuestro primer set (esto es un docstring)

my_set = {'rojo','verde','negro','azul','rojo','azul'} #Se ocupan llaves y no muestra y no incluye los repetidos
print(type(my_set))
print(len(my_set))
print(my_set)

# DICCIONARIOS
mi_mascota = {'tipo':'perro',
              'nombre':'Beba',
              'edad': 4,
              'personalidad': 'amigable'}
print(type(mi_mascota))
print(len(mi_mascota))
print(mi_mascota)

# DICCIONARIO 2
birthdays = {
    'Alice':'Apr 1',
    'Bob': 'Dec 12',
    'Carol':'Mar 4'
}
print(birthdays['Alice']) #PAra extraer información pongo entre corchetes [] la clave que busco

birthdays['Carol'] = 'Sep 12' # Así puedo cambiar un dato
print(birthdays['Carol'])

birthdays['Pau'] = 'Jul 31' #Puedo crear/agregar una variable al diccionario
print(birthdays)

del birthdays['Bob']
print(birthdays)

birthdays.values()

for f in birthdays.values():
    print(f)
    
for n in birthdays.keys():
    print(n)
    
for person, date in birthdays.items():
    print(person,date)
    print(f'El cumpleaños de {person} es el día {date}')