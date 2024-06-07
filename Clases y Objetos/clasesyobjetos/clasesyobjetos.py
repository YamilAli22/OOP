#los atributos son variables que perteneces a una clase

class Celular:
    #metodo o funcion constructora
    def __init__(self, marca, modelo, camara): #self es una forma de hacer referencia a si mismo
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

#un objeto tiene atributos y/o propiedades (marca, modelo, tipo de camara, en este ejemplo)
#y tambien tiene metodos, osea cosas que puede hacer, acciones

celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 13", "50MP")
print(celular1.marca)
print(celular2.modelo)