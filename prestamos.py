# Vamos a crear la primera función
def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):  #Se toma la información de todas las listas
    estudiante_existe = False
    libro_existe = False
    carnet = input('Ingrese su carnet: ').upper()  #Para que el sistema acepte el carnet independientemente si S es mayúscula o no
    for estudiante in lista_estudiantes:     
        if estudiante['Carnet']==carnet:   #Si el carnet ingresado esta registrado continua a la siguiente etapa...
            estudiante_existe = True
    if estudiante_existe == False:
        print('No se ha encontrado al estudiante')  #Pero si no existe el estudiante se muestra este mensaje
    elif estudiante_existe == True:
        codigo = input('Ingrese el código del libro: ').upper()   #Al estudiante existente se le pide el código del libro que quiere registrar 
        for libro in lista_libros:
            if libro['Código del libro'] == codigo:     #Si el código existe se se deja registrar y se pide la fecha
                libro_existe = True
    fecha = input('Ingrese la fecha: ')
    for i in lista_libros:
        if i['Disponibilidad'] == True:
    
            prestamo = {                            #La información completa del registro se guarda en la variable prestamo
                'Carnet':carnet,
                'Código': codigo,
                'Fecha': fecha
                }
            lista_prestamos.append(prestamo)      #Se agrega el prestamo a la lista de prestamos
            libro['Disponibilidad'] = False       #Una vez hecho el prestamos el libro pasa a False, ya que esta prestado            
            print('Prestamo exitoso')
            
# Segunda función

def mostrar_prestamos(lista_prestamos):
    if lista_prestamos == []:
        print('No hay prestamos')            #Se muestran los prestamos, si no existe se muestra un mensaje
    else:
        for prestamo in lista_prestamos:
            print(prestamo['Carnet'],prestamo['Código'],prestamo['Fecha'])   #Pero si existe, se muestra el carnet de quien lo prestó, el código del libro y la fecha
            
        
                
    

    
    