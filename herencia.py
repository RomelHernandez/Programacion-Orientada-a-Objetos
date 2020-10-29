class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a",self.nombre,"de",self.edad)
    
    def hablar (self,*palabras):
        for frase in palabras:
            print(self.nombre,':',frase)


class Deportista(Persona):
    def practicarDeporte (self):
        print(self.nombre,": Voy a practicar")

Juan = Persona(18,"Juan")
Juan.hablar("Hola estoy hablando", "Este soy yo")
Luis = Deportista(20,"Luis")
Luis.hablar("Hola estoy hablando", "Este soy yo")
Luis.practicarDeporte()
    
