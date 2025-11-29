'''lista = ['uno','dos','tres','cuatro']
print(lista[0])
print(lista[1])
nombre = 'Antonio'
print(nombre.lower().count('a'))
print(lista.count('dos'))'''

'''nombres=['Ana','Antonio','José','Ana']
print(nombres.count('Ana'))
print(len(nombres))
print(len(nombres[2]))
print(nombres[0].count('a')) #Esto daría 1 por que el primer elemento es Ana y dentro de Ana hay una 'a'
print(nombres[0].lower().count('a')) #Esto da 2 porque estoy poniendo .lower para poder hacer la palabra minuscula y que ahi me cuente todas las 'a'.
print(nombres.count('a')) #Esto da 0 por que no hay ningun elemento llamado 'a'
print(nombres[0].lower().count('a')+nombres[1].lower().count('a')+nombres[2].lower().count('a')+nombres[3].lower().count('a')) # El resultado es 5 porque es la suma de todas las 'a' que hay en los 4 elementos de la lista.'''

'''nombres = ['Ana','Paulina','Antonio','José']
print(nombres)
nombres[1]='Pablo'
print(nombres)
nombres.append('Hazel') #Agrega el elemento al final de la lista
print(nombres)
nombres.insert(3,'Sebas') #Para agregar en la posición que yo quiera pero es .insert(NUMERO DE POSICION,STRING)
nombres.insert(int(input()),'Sebas') # Con el int(input()) el usuario decide donde agregar el nombre, con otro input puedo elegir el nombre también (luego de la coma)
print(nombres)
nombres.remove('Sebas') #Borra el elemento de la lista
print(nombres)
nombre_borrado= nombres.pop(int(input())-1)
print(nombres)
print(nombre_borrado)'''

nota = float(input())
if nota ==6:            #Al agregar los dos puntos se cambía la tabulación (como la sangría)
    print('Pasó')




  
