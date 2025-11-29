# APLICACIÓN PARA CAFETERÍA (GESTIÓN DE PLATOS Y PEDIDOS) - PAOLA MENÉNDEZ

aplicación = True # Mientras el usuario haga uso de la aplicación se trabajará dentro de ella
agente = 'encargado' # Variable con valor de encargado
platillo = [] # Variable del lista de platillos
precios = [] # Variable de lista de precios

nombre_agente = input('Favor ingrese el nombre del agente: ') # Input para que el usuario ingrese el nombre del agente
while nombre_agente.lower() != agente: # While para indicar que hasta que no se ponga el valor del agente correcto lo siga escribiendo
    print('Agente no registrado') 
    nombre_agente = input('Favor ingrese el nombre del agente: ')
else: 
    while aplicación: # Cuando ya se haya ingresado el agente correcto y aplicación sea True se permitirá ingresar
        opciones = int(input('1. Creación de platillos 2. Consulta de platillos y precios 3. Colocar un pedido 4. Salir: ')) # La variable opciones que permitirá al usuario decidir que opción quiere
        if opciones == 1: # Cuando el usuario elija la opción 1, le aparecerán dos opciones 
            platillo.append(input('Ingrese el nombre del platillo a crear: ').lower()) # La primer opción es ingresar el nombre del platillo
            precios.append(float(input('Ingrese el precio del platillo a crear: '))) # En la segunda opción agregará el precio del platillo
        elif opciones == 2: # Si elije la opción 2 consultará los platillos dentro de la aplicación
            if len(platillo) == 0: # Si no hay ninguno aparecera el mensaje de abajo
                print('Actualmente no hay platillos ingresados')
            else:
                for plato in range(len(platillo)): # Pero si hay platillos, por cada plato en la lista de platillos se imprimirá el platillo elejido junto a su precio
                    print(f'{platillo[plato]}: ${precios[plato]}')
        elif opciones == 3: # Si elije la opción 3, tendrá la opción de colocar un pedido
            platillo_a_elegir = input('Indique el nombre del platillo para su orden: ') # Una variable para el platillo que elijirá dentro de la aplicación
            if platillo_a_elegir.lower() in platillo: # Le pongo lower para que independiente como el usuario ingrese el platillo (mayúscula/minúscula), la aplicación lo reconozca
                orden_platillo = platillo.index(platillo_a_elegir.lower()) # Ahora la aplicación buscará el nombre del platillo dentro de la lista de platillos
                print(f'Usted ha elegido {platillo[orden_platillo]} con un precio de {precios[orden_platillo]}')
            else:
                print('El platillo ingresado no existe') # En dado caso el platillo no exista dentro de la lista aparecera ese mensaje
        elif opciones == 4: # Por último, si el usuario elije la opción 4, la aplicación se ''apagará''
            aplicación = False # Se pone false para que la aplicación/sistema se apague 

    
        
                