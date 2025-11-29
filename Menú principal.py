from MenúCarlitos import menu_carlitos   #Se importa el módulo del menú de Carlitos
from Menúcliente import menu_cliente     #Se exporta el módulo del menú del cliente

catalogo = []
contraseña_de_Carlitos = 'Carlitos123'   #Contraseña definida previamente como una variable
def menu_principal():
    while True:
        print("\n--- BIENVENIDO A DONDE CARLITOS ---")   #Se muestran las opciones que puede elegir el usuario
        print('¿Quién eres?')
        print('1. Soy Carlitos')
        print('2. Soy Cliente')
        print('3. Salir')
        
        opcion = input('Selecciona una opción: ')      #Variable de para elegir la opción
        
        if opcion == '1':                                     #Si se selecciona la opción 1, se escoge entrar como Carlitos
            print('\nHas elegido entrar como Carlitos')
            while True:                                       #El sistema pide la contraseña y si es correcta se abre el menú de Carlitos, pero si no, se vuelve a pedir la contraseña
                contraseña = input('Ingresa la contraseña: ')
                if contraseña == contraseña_de_Carlitos:
                    print('Bienvenido Carlitos')
                    print('¿Qué haras ahora?')
                    menu_carlitos(catalogo)
                    break
                else:
                    print('Contraseña incorrecta')
                    print('Intente de nuevo')
        
        elif opcion == '2':                                      #Si se selecciona la opción 2, se escoge entrar como cliente
            print('\nHas elegido entrar como cliente')
            menu_cliente(catalogo)
            
        elif opcion == '3':
            print('Gracias por venir a Donde Carlitos. ¡Feliz día!')    #Por último, si se selecciona la opción 3, el programa se cierra
            return
        
        else:
            print('La opción no existe. Elige otra.')      #Si se digita una opción que no está dentro del menú aparece el siguiente mensaje
                
menu_principal()  #Aquí se llama a la función
        