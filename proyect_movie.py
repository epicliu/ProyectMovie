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
    cmenu = "S"
    while cmenu == "S":
        id_director = input("Introducir Id de Director: ")
        c.execute("INSERT INTO TB_PeliculaDirector Values('%s', '%s')"%(pelicula_nueva.id_pelicula, id_director))
        cmenu=input("Introducir otro Director? S o N:")
        conn.commit()
    cmenu = "S"
    while cmenu == "S":
        id_productor = input("Introducir Id Productor")
        c.execute("INSERT INTO TB_PeliculaProductor Values('%s', '%s')"%(pelicula_nueva.id_pelicula, id_productor))
        cmenu=input("Introducir otro Productor? S o N:")
        conn.commit()
    cmenu = "S"
    while cmenu == "S":
        id_actor = input("Introducir Id Actor")
        c.execute("INSERT INTO TB_PeliculaActor Values('%s', '%s')"%(pelicula_nueva.id_pelicula, id_actor))
        cmenu=input("Introducir otro Actor? S o N:")
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

def comprobar_persona(id_persona):
    c.execute("SELECT * FROM TB_Persona WHERE id_persona = '%s'" % (id_persona))
    result = str(c.fetchall())
    conn.commit()
    return result

def comprobar_id_tb(nombre_tabla, nombre_id, id_tabla):
    c.execute("SELECT * FROM TB_%s WHERE id_%s = '%s'" % (nombre_tabla, nombre_id, id_tabla))
    result = str(c.fetchall())
    conn.commit()
    return result

def nueva_persona(persona_nueva):
    c.execute("INSERT INTO TB_Persona Values('%s', '%s', '%s', '%s', '%s', %i)" % (persona_nueva.id_persona, persona_nueva.nombre, persona_nueva.apellido, persona_nueva.fecha_nacimiento, persona_nueva.sexo, persona_nueva.altura))
    conn.commit()    

def leer_persona(nombre_tabla, nombre_id):
    cmenu=0
    operacion = {1: 'id_%s' %(nombre_id), 2 : 'nombre', 3: 'apellido', 4: 'edad', 5 : 'sexo', 6 : 'altura', 7: salir_menu}
    while cmenu != 7:
        print("Menu de Busqueda de %s" %(nombre_tabla))
        print("¿Que desea buscar?")
        print("""
        1. Id de %s
        2. Nombre
        3. Apellido
        4. Edad
        5. Sexo
        6. Altura
        7. Salir"""%(nombre_tabla))
        cmenu = int(input())
        if cmenu != 7:
            if cmenu != 6:             
                busqueda = input("Introducir %s: " % (operacion[cmenu]))
                c.execute("SELECT * FROM TB_Persona INNER JOIN TB_%s ON TB_Persona.id_persona = TB_%s.id_persona WHERE %s='%s'" %(nombre_tabla, nombre_tabla,operacion[cmenu], busqueda) )
                result = c.fetchall()
                conn.commit()
                print(result)
            else:
                busqueda = int(input("Introducir %s: " % (operacion[cmenu])))
                c.execute("SELECT * FROM TB_Persona INNER JOIN TB_%s ON TB_Persona.id_persona = TB_%s.id_persona WHERE %s=%i" %(nombre_tabla, nombre_tabla,operacion[cmenu], busqueda) )
                result = c.fetchall()
                conn.commit()
                print(result)                
        else:
            operacion[cmenu]()

def actualizar_persona(nombre_tabla, nombre_id):
    cmenu=0
    operacion = {1 : 'nombre', 2: 'apellido', 3: 'altura', 4 : salir_menu}
    while cmenu != 4:
        print("Menu de Actualizar de %s" % (nombre_tabla))
        print("¿Que desea actualizar?")
        print("""
        1. Nombre
        2. Apellido
        3. Altura
        4. Salir""")
        cmenu = int(input())
        if cmenu != 4:
            id_d = input("Introducir el id del %s: " % (nombre_tabla))
            if cmenu != 3 :             
                cambio = input("Introducir nuevo %s: " % (operacion[cmenu]))
                c.execute("UPDATE TB_Persona  set %s = '%s' WHERE EXISTS ( SELECT * FROM TB_%s WHERE TB_Persona.id_persona = TB_%s.id_persona AND TB_%s.id_%s = '%s')" %(operacion[cmenu], cambio, nombre_tabla, nombre_tabla, nombre_tabla, nombre_id, id_d))
                c.execute("SELECT * FROM TB_Persona INNER JOIN TB_%s ON TB_Persona.id_persona = TB_%s.id_persona WHERE %s='%s'" %(nombre_tabla, nombre_tabla, operacion[cmenu], cambio) )
                result = c.fetchall()
                conn.commit()
                print(result)
            else:
                cambio = int(input("Introducir %s: " % (operacion[cmenu])))
                c.execute("UPDATE TB_Persona  set %s = %i WHERE EXISTS ( SELECT * FROM TB_%s WHERE TB_Persona.id_persona= TB_%s.id_persona AND TB_%s.id_%s = '%s')" %(operacion[cmenu], cambio, nombre_tabla, nombre_tabla, nombre_tabla, nombre_id, id_d))
                c.execute("SELECT * FROM TB_Persona INNER JOIN TB_%s ON TB_Persona.id_persona = TB_%s.id_persona WHERE %s=%i" %(nombre_tabla, nombre_tabla,operacion[cmenu], cambio) )
                result = c.fetchall()
                conn.commit()
                print(result)                
        else:
            operacion[cmenu]()

def eliminar_persona(nombre_tabla, nombre_id):
    print("Eliminar un %s" % (nombre_tabla))
    id_d = input("Introducir el id de %s para eliminar: " % (nombre_tabla))
    c.execute("SELECT id_persona FROM TB_%s WHERE id_%s = '%s'" %(nombre_tabla, nombre_id, id_d))
    id_p = str(c.fetchall())
    c.execute("DELETE FROM TB_%s WHERE id_%s='%s'" % (nombre_tabla, nombre_id, id_d))
    print("Se ah eliminado %s" % (nombre_tabla))    

def nuevo_director():
    id_persona = input("Introducir Id de persona: ")
    if comprobar_persona(id_persona)[1] == ']':
        director_nuevo = TB_Director(id_persona, input("Introducir Nombre de persona: "), input("Introducir Apellido de apellido: "),datetime.date(int(input("Introducir año: ")), int(input("Introducir Mes: ")), int(input("Introducir Dia: "))), input("Introducir sexo F o M: "), int(input("Introducir Altura en cm: ")), input("Introducir ID del director: "))
        nueva_persona(director_nuevo)
        c.execute("INSERT INTO TB_Director Values('%s', '%s')" % (director_nuevo.id_director, director_nuevo.id_persona))
        conn.commit()
    else:
        print("Esa persona ya existe")
        director_nuevo_id_director = input("Introducir Id del Director ")
        c.execute("INSERT INTO TB_Director Values('%s', '%s')" % (director_nuevo_id_director, id_persona))
        conn.commit()

def leer_director():
    leer_persona("Director", "director")

def actualizar_director():
    actualizar_persona("Director", "director")

def eliminar_director():
    eliminar_persona("Director", "director")

def nuevo_productor():
    id_persona = input("Introducir Id de persona: ")
    if comprobar_persona(id_persona)[1] == ']':
        productor_nuevo = TB_Productor(id_persona, input("Introducir Nombre de persona: "), input("Introducir Apellido de apellido: "),datetime.date(int(input("Introducir año: ")), int(input("Introducir Mes: ")), int(input("Introducir Dia: "))), input("Introducir sexo F o M: "), int(input("Introducir Altura en cm: ")), input("Introducir ID del Productor: "))
        nueva_persona(productor_nuevo)
        c.execute("INSERT INTO TB_Productor Values('%s', '%s')" % (productor_nuevo.id_productor, productor_nuevo.id_persona))
        conn.commit()
    else:
        print("Esa persona ya existe")
        productor_nuevo_id_productor = input("Introducir Id del Productor: ") 
        c.execute("INSERT INTO TB_Productor Values('%s', '%s')" % (productor_nuevo_id_productor, id_persona))
        conn.commit()

def leer_productor():
    leer_persona("Productor", "productor")
    
def actualizar_productor():
    actualizar_persona("Productor", "productor")

def eliminar_productor():
    eliminar_persona("Productor", "productor")

def nuevo_actor():
    id_persona = input("Introducir Id de persona: ")
    if comprobar_persona(id_persona)[1] == ']':
        actor_nuevo = TB_Actor(id_persona, input("Introducir Nombre de persona: "), input("Introducir Apellido de apellido: "),datetime.date(int(input("Introducir año: ")), int(input("Introducir Mes: ")), int(input("Introducir Dia: "))), input("Introducir sexo F o M: "), int(input("Introducir Altura en cm: ")), input("Introducir ID del Actor: "))
        nueva_persona(actor_nuevo)
        c.execute("INSERT INTO TB_Actor Values('%s', '%s')" % (actor_nuevo.id_actor, actor_nuevo.id_persona))
        conn.commit()
    else:
        print("Esa persona ya existe")
        actor_nuevo_id_actor = input("Introducir Id del Actor: ") 
        c.execute("INSERT INTO TB_Actor Values('%s', '%s')" % (actor_nuevo_id_actor, id_persona))
        conn.commit()

def leer_actor():
    leer_persona("Actor", "actor")
    
def actualizar_actor():
    actualizar_persona("Actor", "actor")

def eliminar_actor():
    eliminar_persona("Actor", "actor")

def nuevo_genero():
    genero_nuevo = TB_Genero(input("Introducir Id de Genero: "), input("Introducir Nombre de Genero: "))
    c.execute("INSERT INTO TB_Genero Values('%s', '%s')" % (genero_nuevo.id_genero, genero_nuevo.nombre))
    conn.commit()

def leer_genero():
    cmenu=0
    operacion = {1: 'id_genero', 2 : 'nombre', 3 : salir_menu}
    while cmenu != 3:
        print("Menu de Busqueda de Genero")
        print("¿Que desea buscar?")
        print("""
        1. Id de Genero
        2. Nombre
        3. Salir""")
        cmenu = int(input())
        if cmenu != 3:              
            busqueda = input("Introducir %s: " % (operacion[cmenu]))
            c.execute("SELECT * FROM TB_Genero WHERE %s='%s'" %(operacion[cmenu], busqueda) )
            result = c.fetchall()
            conn.commit()
            print(result)       
        else:
            operacion[cmenu]()

def actualizar_genero():
    cmenu=0
    operacion = {1 : 'nombre', 2: salir_menu}
    while cmenu != 4:
        print("Menu de Actualizar de Genero")
        print("¿Que desea actualizar?")
        print("""
        1. Nombre
        2. Salir""")
        cmenu = int(input())
        if cmenu != 2:
            id_g = input("Introducir el id del Genero: ")
            cambio = input("Introducir nuevo %s: " % (operacion[cmenu]))
            c.execute("UPDATE TB_Genero set %s = '%s' where id_genero = '%s'" %(operacion[cmenu], cambio, id_g))
            c.execute("SELECT * FROM TB_Genero WHERE %s='%s'" %(operacion[cmenu], cambio) )
            result = c.fetchall()
            conn.commit()
            print(result)              
        else:
            operacion[cmenu]()

def eliminar_genero():
    print("Eliminar un Genero")
    id_p = input("Introducir el id del Genero para eliminar: ")
    c.execute("DELETE FROM TB_Genero WHERE id_genero='%s'" % (id_p))
    print("Se ah eliminado el Genero")

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
    operacion = {1: nuevo_productor, 2 : leer_productor, 3: actualizar_productor, 4: eliminar_productor, 5 : salir_menu}
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())
        operacion[cmenu]()

def actor_menu():
    cmenu=0
    operacion = {1: nuevo_actor, 2 : leer_actor, 3: actualizar_actor, 4: eliminar_actor, 5 : salir_menu}
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())
        operacion[cmenu]()  

def genero_menu():
    cmenu=0
    operacion = {1: nuevo_genero, 2 : leer_genero, 3: actualizar_genero, 4: eliminar_genero, 5 : salir_menu}
    while cmenu !=5:
        crud_menu()
        cmenu = int(input())
        operacion[cmenu]()  

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
    operacion = {1: pelicula_menu, 2 : director_menu, 3: productor_menu, 4: actor_menu, 5: genero_menu, 6 : salir_menu}
    while cmenu != 6:
        print("Bienvenido al menu")
        print("¿Que desea realizar?")
        print("""
        1. Pelicula
        2. Director
        3. Productor
        4. Actor
        5. Genero
        6. Salir""")
        cmenu = int(input())
        operacion[cmenu]()

menu()