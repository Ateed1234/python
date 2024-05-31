# Lista de tareas usando mysql
import mysql.connector
from mysql.connector import errorcode

option = None

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'port': '3306',
  'database': 'lista',
  'raise_on_warnings': True
}

# Empezar conexion con la base de datos
def conectar_mysql():
  try:
    cnx = mysql.connector.connect(**config)
    return cnx

 
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)


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
    except ValueError as e:
        print("Escoje un numero de la lista.")

# Mostrar lista de tareas
def opcion1(conexion):
  mycursor = conexion.cursor()
  mycursor.execute("select ID,name_tareas  from tareas")
  mylist = mycursor.fetchall()
  for (ID, name_tareas) in mylist:
     print("{}- {}".format(ID, name_tareas))

# Añadir tarea en la base de datos.
def opcion2(conexion):
  añadir_tarea = input('Que tearea quieres añadir a la lista de tareas: ')
  while añadir_tarea == '':
    print('Escribe una tarea para añadir en la lista.')
    añadir_tarea = input('Que tearea quieres añadir a la lista de tareas: ')
  sql = f"INSERT INTO tareas (name_tareas) values ('{añadir_tarea}');"
  mycursor = conexion.cursor()
  mycursor.execute(sql)
  conexion.commit()

# Eliminar tarea de la base de datos
def opcion3(conexion):
  quitar_tarea = int(input('Que tarea quieres elimilar de la lista de tareas: '))
  sql = f"DELETE FROM tareas where ID={quitar_tarea}"
  mycursor = conexion.cursor()
  mycursor.execute(sql)
  conexion.commit()

# Vaciar la base de datos
def opcion4(conexion):
  borrar = ""
  while borrar.lower() != 'si' and borrar != 'no':
    borrar = input('Estas seguro que quieres borrar la lista de tareas? Escribe Si o No: ')
  if borrar.lower() == 'si':
      # Borrat tabla
      sql = "DROP TABLE tareas"
      mycursor = conexion.cursor()
      mycursor.execute(sql)
      conexion.commit()
      # Recrear tabla
      mycursor.execute("""
        CREATE TABLE tareas (
          ID int NOT NULL AUTO_INCREMENT,
          name_tareas varchar(255) NOT NULL,
          PRIMARY KEY (ID)
          )
      """)
      print('Lista de tareas borrada.')                  
  else:
      print('Gracias por confirmar, la lista de tareas no va a ser borrada.')


def main():
    conexion = conectar_mysql()
    global option
    while option != 5:
        option = menu()
        if option == 1:
            opcion1(conexion)
        elif option == 2:
            opcion2(conexion)
        elif option == 3:
            opcion3(conexion)
        elif option == 4:
            opcion4(conexion)

if __name__ == "__main__":
    main()



