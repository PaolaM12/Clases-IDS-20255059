#Aquí se creará el menú del cliente
def menu_cliente(catalogo):                                   #La función se entrelaza con la lista catálogo del menú principal
    nombre_cliente = input('Ingresa tu nombre completo: ')    #Se pide el nombre del cliente
    pedido = []                                               #Se crea una lista para ingresar los productos que el cliente quiere
    while True:                                               #Mientras la función esté activda se muestran las siguientes opciones
        print('1. Ver catálogo')
        print('2. Realizar pedido')
        print('3. Mostrar el pedido y el total')
        print('4. Eliminar producto del pedido')
        print('5. Salir')
        
        opcion = input(f'¡Hola {nombre_cliente}! Selecciona una opción: ')      #Variable para elegir la opción
        
        if opcion == '1':                             #Si se selecciona la opción 1, el cliente puede ver el catálogo de Carlitos 
            if catalogo == []:                            
                print('No hay productos en el catalogo')
            else:
                for prod in catalogo:
                    print(f'{prod['Nombre'].capitalize()} - ${prod['Precio']}')   #De la misma forma se muestra producto-precio con la primer letra de los productos en mayúsculas
        
        elif opcion == '2':                           #Con la opción 2, el cliente puede agregar productos a su pedido
            if catalogo == []:                        #Si el catálogo está vacío, no habrá productos para elegir y se muestra el mensaje
                print('No hay productos en el catálogo')
            else:
                producto_pedido = input('Ingresa el nombre del producto que quieres añadir a tu pedido: ')    
                producto_existe = False
                for prod in catalogo:
                    if prod['Nombre'].lower() == producto_pedido.lower(): #Se busca el producto que el cliente quiero dentro de la lista de catálogo, se aplica la función .lower() para que no afecte como esté escrita 
                        pedido.append(prod)
                        producto_existe = True
                        print('Producto agregado a tu pedido')
                        
                if not producto_existe:
                    print('El producto no existe en el catálogo')   #Si no existe el producto, se muestra el siguiente mensaje
                    
        elif opcion == '3':                                    #Con la opción 3, el cliente puede ver el total a pagar de su pedido y el detalle de este mismo
            if pedido == []:                                   #Si el pedido está vacío y no hay productos agregados se muestra el siguiente mensaje
                print('No hay productos en el pedido')
            else:
                print('\n--- TU PEDIDO ---')                   #Si hay productos dentro del pedido, se muestra el detalle de forma ordenada 
                total = 0                                      #Al inicio el total es 0 
                for producto in pedido:
                    print(f'{producto['Nombre'].capitalize()} - ${producto['Precio']}')
                    total += producto['Precio']                #Mediante se van agregando productos se van sumando sus precios
                print(f'El total a pagar es ${total}')         #Finalmente se muestra el total a pagar
        
        elif opcion == '4':                                    #Si el cliente selecciona la opción 4, puede eliminar productos del pedido
            if pedido == []:                                   #Si el pedido está vacío se muestra el siguiente mensaje
                print('No hay productos en el pedido')
            else:
                producto_eliminar = input('¿Qué producto deseas eliminar? ')
                producto_existe = False
                for producto in pedido:
                    if producto['Nombre'].lower() == producto_eliminar.lower():   #Si el prducto que el cliente quiere eliminar está dentro de la lista pedido, se muestra el mensaje de eliminado exitosamente
                        pedido.remove(producto)
                        producto_existe = True
                        print('Producto eliminado exitosamente')
                if not producto_existe:                                          #Si el producto no existe, se muestra el siguiente mensaje
                    print('El producto no se ha encontrado en tu pedido')
        
        elif opcion == '5':                                                      #Si la opción seleccionada es la 5, el cliente se sale de está función y se le devuelve al menú principal
            print(f'Gracias por visitar Donde Carlitos, {nombre_cliente}. ¡Vuelve pronto!')            #Con el nombre seleccionado se muestra un mensaje de despedida personalizado
            return                                                               #Se utiliza return para devolver al usuario al menú principal
        
        else:
            print('Esa opción no existe')           #Por otro lado, si la opción no existe, se pide seleccionar otra
            print('Seleccione otra opción: ')
                
                    
                
