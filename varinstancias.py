class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a",self.nombre,"de",self.edad)
    
    def hablar (self,*palabras):
        for frase in palabras:
            print(self.nombre,':',frase)

Juan = Persona(18,"Juan")
Juan.hablar("Hola estoy hablando","Este soy yo")
Luis = Persona(20,"Luis")
Luis.hablar("Hola estoy hablando","Este soy yo")