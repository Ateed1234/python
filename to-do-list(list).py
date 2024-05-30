# Programa de Python que sirve para tener una check-list hecha con listas de python
option = None
lista_tareas = ['hola', 'adios','queloque']


def menu():
    print('=========================================')
    print('1- Ver lista de tareas.')
    print('2- Añadir tarea.')
    print('3- Eliminar tarea.')
    print('4- Vaciar lista de tareas.')
    print('5- Salir')
    print('=========================================')
    try:
        option = int(input('Escoje una opcion: '))
        if len(str(option)) != 1:
            print('Escoje un numero de las oprciones anteriores.')
        return option
    except ValueError:
        print('Escoje un numero de la lista.')

def opcion1():
    if len(lista_tareas) == 0:
        print('La lista esta vacia, por favor añade tareas para poder listarlas.')
        quit
    for i in range(len(lista_tareas)):
        print(f"{i+1} {lista_tareas[i]}")

def opcion2():
    añadir = input('Que tearea quieres añadir a la lista de tareas: ')
    while añadir == '':
        print('Escribe una tarea para añadir en la lista.')
        añadir = input('Que tearea quieres añadir a la lista de tareas: ')
    lista_tareas.append(añadir)

def opcion3():     
    quitar = None
    while quitar not in range(len(lista_tareas)):
        if len(lista_tareas) == 0:
            print('La lista de tareas esta vacia, añade tareas para poder borrarlas cuando se completen')
            break
        try:
            quitar = int(input('Que tarea quieres elimilar de la lista de tareas: '))
            while quitar>len(lista_tareas) or quitar == 0:
                print('Escoje un numero que este dentro de la lista para aliminar esa tarea.')
                quitar = int(input('Que tarea quieres elimilar de la lista de tareas: '))
            lista_tareas.pop(quitar-1)
            break
        except ValueError:
            print('Escoje un numero valido que esté dentro de la lista para eliminarlo.')

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