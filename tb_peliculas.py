class TB_Pelicula:
    def __init__(self, id_pelicula, nombre, year, puntuacion):
        self.id_pelicula = id_pelicula
        self.nombre = nombre
        self.year = year
        self.puntuacion = puntuacion


class TB_Persona:
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo

class TB_Director(TB_Persona):
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo, id_director):
        self.id_director = id_director

class TB_Actor(TB_Persona):
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo,id_actor):
        self.id_actor = id_actor

class TB_Productor(TB_Persona):
    def __init__(self, id_persona, nombre, apellido, fecha_nacimiento, sexo,id_productor):
        self.id_productor = id_productor

class TB_Genero:
    def __init__(self, id_genero, nombre):
        self.id_genero = id_genero
        self.nombre = nombre