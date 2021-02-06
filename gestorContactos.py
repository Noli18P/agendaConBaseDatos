import sqlite3
import sys

conection = sqlite3.connect("contactos")
pointer = conection.cursor()

#Crear tabla
#pointer.execute("CREATE TABLE CONTACTOS (NOMBRE_CONTACTO VARCHAR (50), NUMERO_CONTACTO INTEGER)")


def agregarContacto():
    nombre_contacto = input('Ingrese el nombre del contacto: ')
    numero_contacto = int(input("Ingrese el numero del contacto: "))
    
    informacion = [
                (nombre_contacto, numero_contacto)
            ]

    pointer.executemany("INSERT INTO contactos VALUES(?,?)", informacion)
    conection.commit()
    print('----------------------------------------------------------')
    print(f'El contacto {nombre_contacto} ha sido agregado con exito')
    print('----------------------------------------------------------')


def eliminarContacto():
    pass

def verContacto():
    pass

def verTodo():
    pointer.execute("SELECT * FROM contactos")
    lectura_contactos = pointer.fetchall()

    print('Tus contactos son los siguientes: ')
    print('----------------------------------')
    for i in lectura_contactos:
        print(i)
    print('----------------------------------')
    main()


menu = """
Bienvenido a tu gestor de contactos, selecciona una opcion para ejecutar:

    1 - Agregar contacto
    2 - Eliminar contacto
    3 - Ver contacto
    4 - Ver TODOS los contactos
    5 - Salir
"""

def main():
    print(menu)
    seleccion = input()

    if seleccion == '1':
        agregarContacto()
        main()
    elif seleccion == '2':
        pass
    elif seleccion == '3':
        pass
    elif seleccion == '4':
        verTodo()
    elif seleccion == '5':
        print('Adios')
        sys.exit()
    else:
        print('La opcion ingresada no existe')
        main()

main()


conection.close()
