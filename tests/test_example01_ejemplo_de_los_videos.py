from tests.persona_ejemplo_de_los_videso import Persona


class TestExample:

    def test_example01(self):
        print("Hola Mundo")

        una_persona = Persona("Carlos", 20)
        una_persona.hablar()
        una_persona.saltar()
        print(una_persona.nombre)
        print(una_persona.edad)

        otra_persona = Persona("Luis", 21)
        print(otra_persona.nombre)
        otra_persona.hablar()
        otra_persona.saltar()
        print(otra_persona.edad)

