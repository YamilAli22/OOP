#proteger los elementos de una clase, metodos, variables.
class NuevaClase():
    def __init__(self):
        self.__atributo_privado = "Valores" # _ para atributo privado, __ para mas privado xd
    
    def __hablar(self):
        print("Hola como estas?") #metodo privado

#objeto = NuevaClase()
#print(objeto.__hablar)

class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self): #funcion que accede a un valor que en teoria seria privado
        return self._nombre
    
    def set_nombre(self, nuevo_nombre): #funcion para modificar un valor privado
        self._nombre = nuevo_nombre

yamil = Persona("Yamil", 24)
nombre = yamil.get_nombre()
print(nombre)

yamil.set_nombre("Jose Yamil")
nombre = yamil.get_nombre()
print(nombre)
