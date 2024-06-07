#los atributos son variables que perteneces a una clase

class Celular:
    #metodo o funcion constructora, que define las propiedades de nuestro objeto
    def __init__(self, marca, modelo, camara): #self es una forma de hacer referencia a si mismo
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #toda funcion que creamos dentro de una clase, se llama metodo, y seran las acciones
    #que puede hacer nuestro objeto
    def llamar(self): #hay que pasarle el parametro self, el objeto en si mismo
        print(f'Estas haciendo un llamado desde un: {self.modelo}')
    
    def cortar(self):
        print(f'Cortaste la llamada desde un: {self.modelo}')

#un objeto tiene atributos y/o propiedades (marca, modelo, tipo de camara, en este ejemplo)
#y tambien tiene metodos, osea cosas que puede hacer, acciones

#instanciando un objeto de la clase celular y pasandole como argumento sus propiedades
celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 13", "50MP")
print(celular1.marca)
print(celular2.modelo)

#utilizando las acciones que puede hacer nuestro objeto
celular1.llamar()
celular2.cortar()

