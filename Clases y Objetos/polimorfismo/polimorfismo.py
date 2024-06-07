#si un determinado objeto tiene los métodos que nos interesan, nos basta, siendo su tipo irrelevante.
#a Python le dan igual los tipos de los objetos, lo único que le importan son los métodos.
class Pato:
    def parpar(self): 
        print ("Cuac!")
    def plumas(self): 
        print("El pato tiene plumas blancas y grises.")
 
class Persona:
    def parpar(self):
        print ("La persona imita el sonido de un pato.")
    def plumas(self): 
        print ("La persona toma una pluma del suelo y la muestra.")
 
def en_el_bosque(x):
    x.parpar()
    x.plumas()
 
def juego():
    donald = Pato()
    juan = Persona()
    en_el_bosque(donald)
    en_el_bosque(juan)

juego()