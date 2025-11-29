# Vamos a crear la primera función
def registrar_estudiante(lista_estudiantes):
    nombre_estudiante = input('Ingrese su nombre: ').capitalize() # Para que se haga mayúscula la primer letra
    carnet = f'S{len(lista_estudiantes)+1:03}'  # Para que muestre el carnet en formato S001...S002
    estudiante = {
        'Nombre': nombre_estudiante,
        'Carnet': carnet
    }
    lista_estudiantes.append(estudiante) # Para agregar a la lista de estudiantes
    
# Segunda función

def mostrar_estudiantes(lista_estudiantes):
    for estudiante in lista_estudiantes:  # Para cada estudiante registrado en la lista mostrar su nombre y cárnet
        print(f'''
              Nombre: {estudiante['Nombre']}
              Carnet: {estudiante['Carnet']}
              ''')