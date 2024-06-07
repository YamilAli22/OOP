from abc import ABC, abstractclassmethod

#plantilla que nos permite crear personas
class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad


    @abstractclassmethod
    def hacer_actividad(self): #al hacer esto, luego debo si o si implementar la funcion
        pass

    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Mi actividad es: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Mi actividad (trabajo) es: {self.actividad}")

#instanciando la clase Estudiante
yamil = Estudiante("Yamil", 24, "masculino", "vago")
#llamando a la funcion hacer_actividad para que muestre que actividad hago
yamil.presentarse()
yamil.hacer_actividad()

#haciendo lo mismo pero para la clase Trabajador

tito = Trabajador("Tito", 22, "masculino", "vagox2")
tito.presentarse()
tito.hacer_actividad()



