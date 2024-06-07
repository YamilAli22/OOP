#herencia hace referencia a cuando una clase hija obtener todos los metodos y atributos de la clase padre
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario



        

roberto = Empleado("Roberto", 43, "ARGENTINO", "Programador", 2000)

print(roberto.trabajo)

roberto.hablar()