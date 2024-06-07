class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self): #funcion que accede a un valor que en teoria seria privado
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre): #funcion que modifica un valor que en teoria seria privado
        self._nombre = nuevo_nombre
    
    @nombre.deleter 
    def nombre(self): #funcion que elimina un valor que en teoria seria privado
        del self._nombre

yamil = Persona("Yamil", 24)

nombre = yamil.nombre
print(nombre)

yamil.nombre = "Yamil Ali"
nombre = yamil.nombre
print(nombre)

del yamil.nombre
