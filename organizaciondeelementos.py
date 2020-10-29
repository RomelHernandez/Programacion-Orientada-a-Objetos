from tkinter import*

class Interfaz:

    def __init__(self, contenedor):

        self.e1 = Label(contenedor, text= "Etiqueta 1", fg = "black", bg = "white")
        self.e2 = Label(contenedor, text= "Etiqueta 2", fg = "black", bg = "grey")
        self.e3 = Label(contenedor, text= "Etiqueta 3", fg = "black", bg = "green")
            
        self.e1.pack(side = TOP)
        self.e2.pack(side = RIGHT)
        self.e3.pack(side = BOTTOM, fill = X)
        
    

Ventana = Tk()

miniinterfaz = Interfaz(Ventana)

Ventana.mainloop()

