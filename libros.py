# Vamos a crear la primera función
def registrar_libro(lista_libros):
    titulo = input('Ingrese el título del libro: ') #Pide al usuario el título del libro
    autor = input('Ingrese el nombre del autor: ') #Pide al usuario el nombre del autor
    codigo = f'L{len(lista_libros)+1:03}' #Genera un código automaticamente, el :03 es para rellenar con ceros
    disponible = True #Marca el libro como disponible
    libro = {
        'Código del libro': codigo,    #Se completa la información de cada libro
        'Título del libro': titulo,
        'Autor del libro': autor,
        'Disponibilidad': disponible
    }
    lista_libros.append(libro) #Se agrega el libro registrado a la lista de libros
    
# Segunda función de libros

def mostrar_libros(lista_libros):
    for libro in lista_libros:     #Para cada libro en la lista de libros se imprime su información
        print(f'''Código: {libro['Código del libro']}
              Título: {libro['Título del libro']}
              Autor: {libro['Autor del libro']}
              Estado: {libro['Disponibilidad']}''')