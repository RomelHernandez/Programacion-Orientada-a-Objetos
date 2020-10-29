class Persona:
    def __init__(self):
        self.edad = 18
        self.nombre = "Juan"
        print("Se ha creado a",self.nombre,"de",self.edad)
    def hablar (self, palabras="No sé qué decir"):
        print(self.nombre,':',palabras)

Juan = Persona()
Juan.hablar()
Juan.hablar("Hola estoy hablando")


