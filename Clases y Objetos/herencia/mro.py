#mro: method resolution order
class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")


class C(A):
    def hablar(self):
        print("Hola desde C")


class D(B, C):
    pass


d = D()
d.hablar()

#el mro va por prioridades, primero busca un metodo en la clase a la que llamo
#si no lo encuentra, busca en la primer clase de la que hereda, y se queda buscando en esa rama
#si no encuentra, va a la siguiente clase y sus ramas, y así sucesivamente