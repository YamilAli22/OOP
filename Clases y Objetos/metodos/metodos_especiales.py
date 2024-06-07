class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self, otro): #definiendo un operador que suma, un metodo especial
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)
    
yamil = Persona("Yamil", 24)
tito = Persona("tito", 22)

resultado = yamil + tito
print(resultado)