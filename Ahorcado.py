from tkinter import *
from ClaseJuego import ClaseJuego 

class JuegoTk:

    def __init__(self):
        self.ventana=Tk()
        self.EstamosJugando=False
        #------------------------------------------
        self.ObjetoJUego=ClaseJuego()
        self.Texto1=StringVar()
        self.Texto1.set("Bienvenido al juego del Ahorcado")
        self.Texto2=StringVar()
        self.Texto2.set("Presiona ENTER o ESPACIO para iniciar, ESC para salir")
        self.Etiqueta1=Label(self.ventana,textvariable=self.Texto1)
        self.Etiqueta2=Label(self.ventana,textvariable=self.Texto2)
        self.BotonNuevoJuego=Button(self.ventana,text="Nuevo Juego",command=self.JuegoNuevo)
        self.BotonEnviarTexto=Button(self.ventana,text=">>>",command=self.BotonEnviar)
        self.EntradaTexto=Entry(self.ventana)
        #------------------------------------------
        self.Etiqueta1.pack()
        self.Etiqueta2.pack()
        self.BotonNuevoJuego.pack()
        self.EntradaTexto.pack()
        #------------------------------------------
        self.ventana.mainloop()

    def JuegoNuevo(self):
        self.Texto1.set("GAAA")

    def BotonEnviar(self):
        if EstamosJugando:
            pass
        else:
            pass

        

if __name__=="__main__":a=JuegoTk()
