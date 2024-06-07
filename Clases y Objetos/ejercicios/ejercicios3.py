class Personaje():
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**2
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    

batman = Personaje("Batman", 60, 40)
spiderman = Personaje("Spiderman", 60, 50)
spiderbat = batman + spiderman
#y asi se pueden seguir haciendo "fusiones"
print(spiderbat)