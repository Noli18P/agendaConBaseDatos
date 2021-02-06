import sqlite3

conection = sqlite3.connect("contactos")
pointer = conection.cursor()

#Crear tabla
pointer.execute("CREATE TABLE CONTACTOS (NOMBRE_CONTACTO VARCHAR (50), NUMERO_CONTACTO INTEGER)")


def agregarContacto():
    pass

def eliminarContacto():
    pass

def verContacto():
    pass

def main():
    pass



conection.close()
