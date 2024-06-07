#funcion especial que "decora" a otra
def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola mundo")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

#ahora la forma optima

@decorador
def saludo():
    print("Hola mundo")

saludo()