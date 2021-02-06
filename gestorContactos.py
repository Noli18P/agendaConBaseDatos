import sqlite3
import sys

conection = sqlite3.connect("contactos")
pointer = conection.cursor()

#Crear tabla
#pointer.execute("CREATE TABLE CONTACTOS (NOMBRE_CONTACTO VARCHAR (50), NUMERO_CONTACTO INTEGER)")


def agregarContacto():
    pass

def eliminarContacto():
    pass

def verContacto():
    pass

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
    


conection.close()
