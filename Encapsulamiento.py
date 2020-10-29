class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a",self.nombre,"de",self.edad)
    
    def hablar (self,*palabras):
        for frase in palabras:
            print(self.nombre,':',frase)


class Deportista(Persona):

    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte
        print("Se ha creado a",self.nombre,"de",self.edad)
    
    def practicarDeporte (self):
        print(self.nombre,": Voy a practicar")
    
    def verMiDeporte(self):
        return self.__deporte

Juan = Persona(18,"Juan")
Juan.hablar("Hola estoy hablando", "Este soy yo")
Luis = Deportista(20,"Luis","natación")
Luis.hablar("Hola estoy hablando", "Este soy yo")
Luis.practicarDeporte()
print("Luis practica", Luis.verMiDeporte())