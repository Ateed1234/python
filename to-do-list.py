# Programa de Python que sirve para tener una check-list
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
    option = int(input('Escoje una opcion: '))
    return option

def main():
    global lista_tareas 
    global option
    while option != 5:
        option = menu()
        if option == 1:
            for i in range(len(lista_tareas)):
                print(f"{i+1} {lista_tareas[i]}")
        elif option == 2:
            añadir = input('Que tearea quieres añadir a la lista de tareas: ')
            lista_tareas.append(añadir)
        elif option == 3:
            quitar = input('Que tarea quieres elimilar de la lista de tareas: ')
            lista_tareas.remove(quitar)
        elif option == 4:
            borrar = ""
            while borrar != 'Si' and borrar != 'No':
                borrar = input('Estas seguro que quieres borrar la lista de tareas? ')
            if borrar == 'Si':
                lista_tareas.clear()                  
            elif borrar == 'No':
                print('Gracias por confirmar, la lista de tareas no va a ser borrada.')
            else:
                print('Confirma si vaciar la lista de tareas o no.')
    

if __name__ == "__main__":
    main()