class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f"Hola soy {self.nombre}, soy {self.nacionalidad}, y trabajo en {self.empresa}. {self.mostrar_habilidad()}" #con super accedo al metodo de la clase padre, si usara self estaria accediendo al metodo de esta clase(hija), si es q este existiera


roberto = EmpleadoArtista("Roberto", 52, "argentino", "cantar", 2000, "Google")

presentacion = roberto.presentarse()
print(presentacion)

herencia = issubclass(EmpleadoArtista, Artista) #Para saber si una clase es es subclase de otra, osea si es su hija
print(herencia)

instancia = isinstance(roberto, Artista) #para ver si una variable es una instancia de una clase
print(instancia)