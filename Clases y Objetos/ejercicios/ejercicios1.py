#creando la clase
class Estudiante:
    #dandole atributos con el metodo constructor init
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    #creando un metodo que tendra la clase (una accion que podra realizar el objeto)
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

nombre_estudiante = input("Diga su nombre: ")
edad_estudiante = input("Diga su edad: ")
grado_estudiante = input("Diga su grado: ")
estudiante = Estudiante(nombre_estudiante, edad_estudiante, grado_estudiante)

estudiar = input()
if (estudiar.lower() == "estudiar"):
    estudiante.estudiar()


    
