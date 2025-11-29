clientes = []
cliente = {'Código Cliente': input('Ingresa tu código único: '),
                        'Nombre':input('Ingresa tu nombre completo: '),
                        'Correo':input('Ingresa tu correo electrónico: '),
                        'Teléfono': input('Ingresa tu número de teléfono: ')}

clientes.append(cliente)

menú_productos = []
producto = {'Código Producto': input('Ingrese el código único de su producto: '),
                  'Nombre': input('Ingrese el nombre de su producto: '),
                  'Categoría': input('Ingrese la categoría de su producto: '),
                  'Precio': float(input('Ingrese el precio de su producto : $'))}
menú_productos.append(producto)
   