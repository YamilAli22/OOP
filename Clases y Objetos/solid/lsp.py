#lsp: principio de sustitucion de Liskov's
# class Ave():
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
    

# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pinguino()))

#reconstruyendo lo de arriba para aplicar el principio

class Ave():
    pass

class AveVoladora(Ave):
    def volar(self):
        return "EStoy volando"
    
class AveNoVoladora(Ave):
    pass

#asi, en ave se definirian las cosas que todas las aves tienen en comun, y se crean subclases
#para cosas mas especificas de diferentes aves