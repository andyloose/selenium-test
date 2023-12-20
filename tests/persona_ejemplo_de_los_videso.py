class Persona:

    nombre = None
    dni = None
    edad = None

    def __init__(self, un_nombre, la_edad):
        self.nombre = un_nombre
        self.edad = la_edad

    def hablar(self):
        print("Hola")

    def saltar(self):
        print("Salto")