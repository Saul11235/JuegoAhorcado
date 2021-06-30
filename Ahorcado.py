from ClaseJuego import ClaseJuego 
from tkinter import *

class JuegoGUI:

    def __init__(self):
        self.juego=ClaseJuego()
        self.primerjuego=True
        self.EstamosJugando=False
        self.ventana=Tk()
        
    def maquetarVentana(self):
        self.botonReinicio=Button(self.ventana,text="Nuevo Juego",command=lambda:self.NuevoJuego()).pack()
        self.EtiquetaTexto=Label(self.ventana,text="P A L A B R A").pack()
        self.EtiquetaTexto=Label(self.ventana,text="tus jugadas son").pack()
        self.BotonEnviar=Button(self.ventana,text="texto",command=lambda:self.enviarTexto()).pack()
        pass

    def LanzarPantalla(self): self.maquetarVentana(); self.ventana.mainloop()    

    def ActualizarPantalla(self):
        pass

    def enviarTexto(self):
        print("texto enviado")
        pass

    def NuevoJuego(self):
        print("nuevo juego creado")
        self.juego.nuevojuego()


if __name__=="__main__":
    j=JuegoGUI().LanzarPantalla()

