# Aquí se creará el menú de Carlitos
def menu_carlitos(catalogo):
    while True:                           #Mientras la función este activa se muestran las siguientes funciones y el menú funciona
        print('1. Agregar productos')
        print('2. Eliminar productos')
        print('3. Cambiar precio')
        print('4. Ver catálogo')
        print('5. Salir')
        
        opcion = input('Selecciona una opción Carlitos: ')  #Variable para elegir la opción
        
        if opcion == '1':                                   #La opción 1 permite agregar productos y su precio por medio de un diccionario
            print('¿Qué producto vas a agregar?')
            nombre_producto_agregar = input('Ingresa el nombre de tu producto: ')
            precio = float(input('Ingresa el precio del producto: '))
            producto = {                   
                'Nombre': nombre_producto_agregar,
                'Precio': precio
            }
            catalogo.append(producto)                  #Se agrega al catálogo por medio de .append()
            print('Producto agregado exitosamente')
            
        elif opcion == '2':                           #La opción 2 permite eliminar productos del catálogo
            if catalogo == []:                        #Si la lista de catálogo está vacía se imprime el siguiente mensaje
                print('No hay productos en el catálogo')
            else:
                print('¿Qué producto vas a eliminar?')            
                nombre = input('Ingresa el nombre del producto que eliminarás:  ')
                producto_existe = False
                for prod in catalogo:
                    if prod['Nombre'].lower() == nombre.lower():          #El sistema busca el producto que se desea eliminar en el catálogo, .lower() se incluye para que encunetre el producto independientemente como se escriba (may/min)
                        catalogo.remove(prod)                             #Si la búsqueda es efectiva se remueve del catálogo
                        producto_existe = True
                        print('Producto eliminado exitosamente')
                if not producto_existe:                                   #Si no se encuentra el producto significa que no existe en el catálogo
                    print('El producto no existe en el catálogo')
        
        elif opcion == '3':                                               #Si se selecciona la opción 3, Carlitos puede cambiar el precio
            if catalogo == []:                                            #Si el catálogo está vacío, se muestra el siguiente mensaje
                print('No hay productos en el catálogo')
            else:
                print('¿Cuál es el producto al que le cambiarás el precio?')                             
                nombre_cambio_precio = input('Ingresa el nombre del producto para cambiarle el precio: ')
                producto_existe = False
                for prod in catalogo:
                    if prod['Nombre'].lower() == nombre_cambio_precio.lower():        #Si el producto que se ingresa se encuentra en el catálogo, permite cambiar el precio de ese producto
                        nuevo_precio = float(input('Ingresa el nuevo precio: '))
                        prod['Precio'] = nuevo_precio                                 #Aquí se actualiza en el catálogo
                        producto_existe = True
                        print('El precio se ha cambiado exitosamente')
                if not producto_existe:                                               #Si no se encuentra el producto, no existe y se muestra el siguiente mensaje
                    print('El producto no existe en el catálogo')     
        
        elif opcion == '4':                                      #Si se selecciona la opción 4, Carlitos puede ver el catálogo
            if catalogo == []:                                   #Si no hay productos, se muestra el siguiente mensaje
                print('No hay productos en el catálogo')
            else:
                for prod in catalogo:                           #Por cada producto en la lista de catálogo se imprime el producto - precio
                    print(f'{prod['Nombre'].capitalize()} - ${prod['Precio']}' )   #Se aplica mayúscula a la primer letra de cada producto
        
        elif opcion == '5':                                   #Si se selecciona la opción, el sistema devuelve a Carlitos al menú principal
            print('Hasta la próxima Carlitos...')
            return                                           #Se pone return para que devuelva al menú principal
        
        else:
            print('Esa opción no existe')           #Si se selecciona una opción que no es del menú se pide que ingrese otra
            print('Seleccione otra opción: ')
    
                