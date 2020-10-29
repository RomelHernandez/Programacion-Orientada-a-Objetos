from tkinter import *

class Interfaz:

    def __init__(self, contenedor):

        self.e1 = Label(contenedor, text= "Etiqueta 1", fg = "black", bg = "white")
        self.e1.place(x= 20, y = 30, width = 120, height = 25)


Ventana = Tk()
miniinterfaz = Interfaz(Ventana)
Ventana.mainloop()
