# Programa de Python que sirve para tener una check-list hechas con diccionarios de python
option = None
lista_tareas = {'1':'hola', '2':'adios','3':'queloque'}


def menu():
    print('=========================================')
    print('1- Ver lista de tareas.')
    print('2- Añadir tarea.')
    print('3- Eliminar tarea.')
    print('4- Vaciar lista de tareas.')
    print('5- Salir')
    print('=========================================')
    option = int(input('Escoje una opcion: '))
    if len(str(option)) != 1:
        print('Escoje un numero de las oprciones anteriores.')
    return option

def main():
    global lista_tareas 
    global option
    while option != 5:
        option = menu()
        if option == 1:
            for key,value in lista_tareas.items():
                print(f"{key}- {value}")
        elif option == 2:
            tarea_añadir = input('Que tearea quieres añadir a la lista de tareas: ')
            num_tarea_añadir = len(lista_tareas) +1
            lista_tareas.update({num_tarea_añadir:tarea_añadir})
        elif option == 3:
            reordered_tasks = {}
            new_key = 1
            quitar = (input('Que tarea quieres elimilar de la lista de tareas: '))
            lista_tareas.pop(quitar)
            for key in sorted(lista_tareas.keys()):
                reordered_tasks[new_key] = lista_tareas[key]
                new_key +=1
            return reordered_tasks
        elif option == 4:
            borrar = ""
            while borrar != 'Si' and borrar != 'No':
                borrar = input('Estas seguro que quieres borrar la lista de tareas? ')
            if borrar == 'Si':
                lista_tareas.clear()                  
            elif borrar == 'No':
                print('Gracias por confirmar, la lista de tareas no va a ser borrada.')
            else:
                print('Confirma si quieres vaciar la lista de tareas o no.')
    

if __name__ == "__main__":
    main()