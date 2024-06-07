#dip: principio de inversion de dependencias 
#los modulos de alto y bajo nivel deben depender de las abstracciones
#y los detalles depender de las abstracciones

# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #logica para verificar palabras ... 
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self, texto):
#         #usamos el diccionario para corregir el texto
#         pass
#asi estamos violando el principio porque la clase mas "grande" depende de otra mas "chica"
#hagamoslo bien:
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass

class CorrectorOrtografico:
     def __init__(self, verificador):
        self.verificador = verificador

     def corregir_texto(self, texto):
        #usamos el verificador para corregir el texto
       pass

#ahora CorrectorOrtografico esta dependiendo de la abstraccion del verificador, osea de su implementacion