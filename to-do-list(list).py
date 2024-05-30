# Programa de Python que sirve para tener una check-list hecha con listas de python
option = None
lista_tareas = ['hola', 'adios','queloque']

#Printear menu de opciones y escojer una opcion
def menu():
    print(' ')
    print('=========================================')
    print('1- Ver lista de tareas.')
    print('2- Añadir tarea.')
    print('3- Eliminar tarea.')
    print('4- Vaciar lista de tareas.')
    print('5- Salir')
    print('=========================================')
    print(' ')
    try:
        option = int(input('Escoje una opcion: '))
        if len(str(option)) != 1:
            print('Escoje un numero de las oprciones anteriores.')
        return option
    except ValueError:
        print('Escoje un numero de la lista.')

# Mostrar lista de tareas
def opcion1():
    if len(lista_tareas) == 0:
        print('La lista esta vacia, por favor añade tareas para poder listarlas.')
        quit
    print(' ')
    for i in range(len(lista_tareas)):
        print(f"{i+1} {lista_tareas[i]}")

# Añadir tarea a la lista
def opcion2():
    añadir_tarea = input('Que tearea quieres añadir a la lista de tareas: ')
    while añadir_tarea == '':
        print('Escribe una tarea para añadir en la lista.')
        añadir_tarea = input('Que tearea quieres añadir a la lista de tareas: ')
    lista_tareas.append(añadir_tarea)
    print('Nueva tarea añadida en la lista')

# Eliminar tarea de la lista
def opcion3():     
    quitar_tarea = None
    while quitar_tarea not in range(len(lista_tareas)):
        if len(lista_tareas) == 0:
            print('La lista de tareas esta vacia, añade tareas para poder borrarlas cuando se completen')
            break
        try:
            quitar_tarea = int(input('Que tarea quieres elimilar de la lista de tareas: '))
            while quitar_tarea>len(lista_tareas) or quitar_tarea == 0:
                print('Escoje un numero que este dentro de la lista para aliminar esa tarea.')
                opcion1()
                quitar_tarea = int(input('Que tarea quieres elimilar de la lista de tareas: '))
            lista_tareas.pop(quitar_tarea-1)
            print('Tarea eliminada de la lista.')
            break
        except ValueError:
            confirmar_opcion = input('Seguro que quires eliminar una tarea? ')
            if confirmar_opcion.lower() == 'no':
                break 
            print('Escoje un numero valido de que esté dentro de la siguiente lista para eliminarlo:')
            opcion1()           

# Vaciar lista de tareas
def opcion4():
    borrar = ""
    while borrar.lower() != 'si' and borrar != 'no':
        borrar = input('Estas seguro que quieres borrar la lista de tareas? Escribe Si o No: ')
    if borrar.lower() == 'si':
        lista_tareas.clear()
        print('Lista de tareas borrada.')                  
    else:
        print('Gracias por confirmar, la lista de tareas no va a ser borrada.')


def main():
    global lista_tareas 
    global option
    while option != 5:
        option = menu()
        if option == 1:
            opcion1()
        elif option == 2:
            opcion2()
        elif option == 3:
            opcion3()
        elif option == 4:
            opcion4()
    

if __name__ == "__main__":
    main()