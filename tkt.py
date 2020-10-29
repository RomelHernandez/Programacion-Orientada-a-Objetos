from tkinter import*

class Interfaz:

    def __init__(self, contenedor):

        self.e1 = Label(contenedor, text= "Etiqueta 1", fg = "black", bg = "white")
            
        self.e1.pack()

Ventana = Tk()

miniinterfaz = Interfaz(Ventana)

Ventana.mainloop()

