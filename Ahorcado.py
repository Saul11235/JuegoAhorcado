from tkinter import *
from ClaseJuego import ClaseJuego 

juego=ClaseJuego()


ventana=Tk()

ventana.title("Juego del ahorcado")
ventana.resizable(width=False,height=False)
ventana.geometry("600x300")

BotonNuevoJuego=Button(ventana,text="Nuevo Juego",command=lambda:NuevoJuego()).pack()
Letrero=Label(ventana,text="hola").pack()


def EnviarTexto():
    print("algo copado")

def NuevoJuego():
    print("nuevo juego")
    print(Letrero)
    juego.nuevojuego()


ventana.mainloop()
