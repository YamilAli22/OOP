#ocp: open/closed priciple/principio de abierto/cerrado
#SI SE QUE EN UN FUTURO DEBO AGREGARLE MAS FUNCIONALIDADES A ALGO, TENGO QUE DEJAR UN SISTEMA
#ABIERTO PARA AGREGAR FUNCIONES PERO NO PARA MODIFICARLO
class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.sms}")