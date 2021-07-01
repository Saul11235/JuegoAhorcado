from tkinter import *
from ClaseJuego import ClaseJuego 

class JuegoTk:

    def __init__(self):
        self.ventana=Tk()
        self.ventana.bind("<Return>",lambda x: self.BotonEnviar())
        self.ventana.bind("<Control_R>",lambda x: self.JuegoNuevo())
        self.ventana.bind("<Control_L>",lambda x: self.JuegoNuevo())
        self.ventana.bind("<Escape>",lambda x: exit())
        self.ventana.resizable(width=False,height=False)
        self.ventana.geometry("300x600")
        self.ventana.title("Juego del Ahorcado")
        self.EstamosJugando=False
        #------------------------------------------
        self.ObjetoJuego=ClaseJuego()
        self.Texto1=StringVar()
        self.Texto1.set("Bienvenido al juego del Ahorcado")
        self.Texto2=StringVar()
        self.Texto2.set("Presiona ENTER o CONTROL para juego nuevo, ESC para salir")
        self.Etiqueta1=Label(self.ventana,textvariable=self.Texto1)
        self.Etiqueta2=Label(self.ventana,textvariable=self.Texto2)
        self.BotonNuevoJuego=Button(self.ventana,text="Nuevo Juego",command=self.JuegoNuevo)
        self.BotonEnviarTexto=Button(self.ventana,text=">>>",command=self.BotonEnviar)
        self.EntradaTexto=Entry(self.ventana)
        self.Lienzo=Canvas(self.ventana,width=400,height=300,bg="dark green")
        #------------------------------------------
        self.Etiqueta1.pack()
        self.Etiqueta2.pack()
        self.BotonNuevoJuego.pack()
        self.EntradaTexto.pack()
        self.EntradaTexto.focus_set()
        self.BotonEnviarTexto.pack()
        self.Lienzo.pack()
        #------------------------------------------
        self.ventana.mainloop()

    def JuegoNuevo(self):
        self.Texto1.set("GAAA")
        self.EstamosJugando=True
        self.ObjetoJuego.nuevojuego()
        self.EntradaTexto.focus_set()
        self.__ActualizarVista()

    def BotonEnviar(self):
        if self.EstamosJugando:
            self.ObjetoJuego.jugar(self.EntradaTexto.get())
            if self.ObjetoJuego.getVictoria() or not(self.ObjetoJuego.getJugadorEstaVivo()):
                self.EstamosJugando=False
            self.__ActualizarVista()
            print("Enviado")
        else:
            self.JuegoNuevo()
        self.EntradaTexto.delete(0,"end")    

    def __ActualizarVista(self):
        if self.EstamosJugando:
            letrero=""
            for x in self.ObjetoJuego.getLetrero(): letrero+=x+" "
            self.Texto1.set(letrero)
            mensaje="Tus jugadas: "
            for x in self.ObjetoJuego.getLetrasUsadas():mensaje+=x
            self.Texto2.set(mensaje)
        else:
            if self.ObjetoJuego.getVictoria():
                self.Texto1.set("!Felicidades Has ganado¡ :) ")
                self.Texto2.set("La palabra es "+self.ObjetoJuego.getPalabra())
            else:
                self.Texto1.set("Lo siento, perdiste :( ")
                self.Texto2.set("La palabra era "+self.ObjetoJuego.getPalabra())

    def __Dibujo(self):
        pass 

if __name__=="__main__":a=JuegoTk()
