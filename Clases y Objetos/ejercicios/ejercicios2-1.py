class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"El nombre es: {self.nombre}, la edad es: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"El grado es: {self.grado}")

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
grado = input("Ingrese su grado: ")

estudiante = Estudiante(nombre, edad, grado)

estudiante.mostrar_datos()
estudiante.mostrar_grado()