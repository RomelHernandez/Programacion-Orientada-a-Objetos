from abc import ABCMeta, abstractmethod
class Persona:
    __metaclass__ = ABCMeta


    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a",self.nombre,"de",self.edad)
    
    @abstractmethod
    def hablar (self): pass
    
class Deportista(Persona):

    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte
        print("Se ha creado a",self.nombre,"de",self.edad)
    
    def practicarDeporte (self):
        print(self.nombre,": voy a practicar")
    
    def verMiDeporte(self):
        return self.__deporte
    def hablar(self,*palabras):
        for frase in palabras:
            print(self.nombre,":", frase)

Luis = Deportista(20,"Luis", "Hockey")
Luis.hablar("Hola estoy hablando", "Este soy yo")
Luis.practicarDeporte()
print("Luis practica", Luis.verMiDeporte())
    