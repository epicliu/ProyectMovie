import datetime

class TB_Pelicula:
    def __init__(self, id_pelicula, nombre, year, puntuacion, lista_actores):
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
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, id_director):
        self.id_director = id_director
    
    def nuevo_director(self):
        self.id_director = input("Introducir Id de director: ")

class TB_Actor(TB_Persona):
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo,id_actor):
        self.id_actor = id_actor

class TB_Productor(TB_Persona):
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, id_productor):
        self.id_productor = id_productor

class TB_Genero:
    def __init__(self, id_genero, nombre):
        self.id_genero = id_genero
        self.nombre = nombre


def nueva_pelicula():
    id_pelicula = input("Introducir Id de pelicula: ")
    nombre = input("Introducir Nombre de pelicula: ")
    year = int(input("Introducir Año de pelicula: "))
    puntuacion = input("Introducir Puntuacion de pelicula: ")

def nueva_persona():
    id_persona = input("Introducir Id de persona: ")
    nombre = input("Introducir Nombre de persona: ")
    apellido = input("Introducir Apellido de apellido: ")
    fecha_nacimiento = datetime.date(int(input("Introducir año: ")), int(input("Introducir Mes: ")), int(input("Introducir Dia: ")))
    sexo = input("Introducir sexo F o M: ")
    altura = int(input("Introducir Altura en cm: "))

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
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())

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