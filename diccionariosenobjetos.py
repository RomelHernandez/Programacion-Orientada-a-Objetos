class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a",self.nombre,"de",self.edad)
    
    def hablar (self,**palabras):
        for frase in palabras:
            print(self.nombre,':',palabras[frase])

Juan = Persona(18,"Juan")
Juan.hablar(T1="Hola estoy hablando", T2="Este soy yo")
Luis = Persona(20,"Luis")
Luis.hablar(T1="Hola estoy hablando", T2="Este soy yo")