import sqlite3
import datetime
conn = sqlite3.connect('DB_Proyect_Movie.db')
c = conn.cursor()

class TB_Pelicula:
    def __init__(self, id_pelicula, nombre, year, puntuacion):
        self.id_pelicula = id_pelicula
        self.nombre = nombre
        self.year = year
        self.puntuacion = puntuacion
        self.lista_actores = []
   
class TB_Persona:
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, altura):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.altura = altura

class TB_Director(TB_Persona):
    def __init__(self,  id_persona, nombre, apellido, fecha_nacimiento, sexo, altura, id_director):
        TB_Persona.__init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, altura) 
        self.id_director = id_director
    
class TB_Actor(TB_Persona):
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, altura,id_actor):
        TB_Persona.__init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, altura)
        self.id_actor = id_actor

class TB_Productor(TB_Persona):
    def __init__(self,  id_persona, nombre, apellido, fecha_nacimiento, sexo, altura, id_productor):
        TB_Persona.__init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, altura)
        self.id_productor = id_productor

class TB_Genero:
    def __init__(self, id_genero, nombre):
        self.id_genero = id_genero
        self.nombre = nombre


def nueva_pelicula():
    pelicula_nueva = TB_Pelicula(input("Introducir Id de pelicula: "), input("Introducir Nombre de pelicula: "), int(input("Introducir Año de pelicula: ")), int(input("Introducir Puntuacion de pelicula: ")))
    c.execute("INSERT INTO TB_Pelicula Values('%s', '%s', %i, %i)" % (pelicula_nueva.id_pelicula, pelicula_nueva.nombre, pelicula_nueva.year, pelicula_nueva.puntuacion))
    conn.commit()


def leer_pelicula():
    cmenu=0
    operacion = {1: 'id_pelicula', 2 : 'nombre', 3: 'año', 4: 'puntuacion', 5 : salir_menu}
    while cmenu != 5:
        print("Menu de Busqueda de Pelicula")
        print("¿Que desea buscar?")
        print("""
        1. Id de pelicula
        2. Nombre
        3. Año
        4. Puntuacion
        5. Salir""")
        cmenu = int(input())
        if cmenu != 5:
            if cmenu != 3 and cmenu != 4:             
                busqueda = input("Introducir %s: " % (operacion[cmenu]))
                c.execute("SELECT * FROM TB_Pelicula WHERE %s='%s'" %(operacion[cmenu], busqueda) )
                result = c.fetchall()
                conn.commit()
                print(result)
            else:
                busqueda = int(input("Introducir %s: " % (operacion[cmenu])))
                c.execute("SELECT * FROM TB_Pelicula WHERE %s=%i" %(operacion[cmenu], busqueda) )
                result = c.fetchall()
                conn.commit()
                print(result)                
        else:
            operacion[cmenu]()


def actualizar_pelicula():
    cmenu=0
    operacion = {1 : 'nombre', 2: 'año', 3: 'puntuacion', 4: salir_menu}
    while cmenu != 4:
        print("Menu de Actualizar de Pelicula")
        print("¿Que desea actualizar?")
        print("""
        1. Nombre
        2. Año
        3. Puntuacion
        4. Salir""")
        cmenu = int(input())
        if cmenu != 4:
            id_p = input("Introducir el id de la pelicula: ")
            if cmenu == 1:             
                cambio = input("Introducir nuevo %s: " % (operacion[cmenu]))
                c.execute("UPDATE TB_Pelicula set %s = '%s' where id_pelicula = '%s'" %(operacion[cmenu], cambio, id_p))
                c.execute("SELECT * FROM TB_Pelicula WHERE %s='%s'" %(operacion[cmenu], cambio) )
                result = c.fetchall()
                conn.commit()
                print(result)
            else:
                cambio = int(input("Introducir %s: " % (operacion[cmenu])))
                c.execute("UPDATE TB_Pelicula set %s = %i where id_pelicula = '%s'" %(operacion[cmenu], cambio, id_p))
                c.execute("SELECT * FROM TB_Pelicula WHERE %s=%i" %(operacion[cmenu], cambio) )
                result = c.fetchall()
                conn.commit()
                print(result)                
        else:
            operacion[cmenu]()

def eliminar_pelicula():
    print("Eliminar una pelicula")
    id_p = input("Introducir el id de pelicula para eliminar: ")
    c.execute("DELETE FROM TB_Pelicula WHERE id_pelicula='%s'" % (id_p))
    print("Se ah eliminado la pelicula")



def nuevo_director():
    director_nuevo = TB_Director(input("Introducir Id de persona: "), input("Introducir Nombre de persona: "), input("Introducir Apellido de apellido: "),datetime.date(int(input("Introducir año: ")), int(input("Introducir Mes: ")), int(input("Introducir Dia: "))), input("Introducir sexo F o M: "), int(input("Introducir Altura en cm: ")), input("Introducir ID del director: "))
    c.execute("INSERT INTO TB_Persona Values('%s', '%s', '%s', '%s', '%s', %i)" % (director_nuevo.id_persona, director_nuevo.nombre, director_nuevo.apellido, director_nuevo.fecha_nacimiento, director_nuevo.sexo, director_nuevo.altura))
    c.execute("INSERT INTO TB_Director Values('%s', '%s')" % (director_nuevo.id_director, director_nuevo.id_persona))
    conn.commit()


def leer_director():
    print("leer")

def actualizar_director():
    print("actualizar")

def eliminar_director():
    print("eliminar")

def salir_menu():
    print("Saliendo......")

def pelicula_menu():
    cmenu=0
    operacion = {1: nueva_pelicula, 2 : leer_pelicula, 3: actualizar_pelicula, 4: eliminar_pelicula, 5 : salir_menu}
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())
        operacion[cmenu]()


def director_menu():
    cmenu=0
    operacion = {1: nuevo_director, 2 : leer_director, 3: actualizar_director, 4: eliminar_director, 5 : salir_menu}
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())
        operacion[cmenu]()

def productor_menu():
    cmenu=0
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())

def actor_menu():
    cmenu=0
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())  


def crud_menu():
    print("¿Que desea realizar?")
    print("""
    1. Crear
    2. Leer
    3. Actualizar
    4. Eliminar
    5. Salir""")

def menu():
    cmenu= 0
    operacion = {1: pelicula_menu, 2 : director_menu, 3: productor_menu, 4: actor_menu, 5 : salir_menu}
    while cmenu != 5:
        print("Bienvenido al menu")
        print("¿Que desea realizar?")
        print("""
        1. Pelicula
        2. Director
        3. Productor
        4. Actor
        5. Salir""")
        cmenu = int(input())
        operacion[cmenu]()


menu()