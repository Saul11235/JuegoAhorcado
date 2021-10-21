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
        self.ventana.geometry("920x300")
        self.ventana.title("Juego del Ahorcado por Saul11235/Edwin Saul")
        self.EstamosJugando=False
        #------------------------------------------
        self.ObjetoJuego=ClaseJuego()
        self.Texto1=StringVar()
        self.Texto1.set("Bienvenido al juego del Ahorcado")
        self.Texto2=StringVar()
        self.Texto2.set("ENTER o CTRL para juego nuevo, ESC para salir")
        self.Etiqueta1=Label(self.ventana,textvariable=self.Texto1,width=30,height=2)
        self.Etiqueta2=Label(self.ventana,textvariable=self.Texto2,width=40,height=2)
        self.BotonNuevoJuego=Button(self.ventana,text="Nuevo Juego",command=self.JuegoNuevo)
        self.BotonEnviarTexto=Button(self.ventana,text=">>>",command=self.BotonEnviar)
        self.EntradaTexto=Entry(self.ventana,width=3)
        self.Lienzo=Canvas(self.ventana,width=300,height=300,bg="dark green")
        #------------------------------------------
        #Estilos y maquetacion
        self.Etiqueta1.grid(row=0,column=1,columnspan=3)
        self.Etiqueta2.grid(row=1,column=1,columnspan=3)
        self.BotonNuevoJuego.grid(row=2,column=3)
        self.EntradaTexto.grid(row=2,column=2)
        self.EntradaTexto.focus_set()
        self.BotonEnviarTexto.grid(row=2,column=1)
        self.Lienzo.grid(row=0,column=0,rowspan=3)
        #------------------------------------------
        self.Etiqueta1.config(fg="blue4",font=("Verdana",20))
        self.Etiqueta2.config(fg="red4",font=("Verdana",18))
        self.BotonNuevoJuego.config(font=("Verdana",14))
        self.EntradaTexto.config(fg="green2",bg="black",font=("Verdana",30))
        self.BotonEnviarTexto.config(font=("Verdana",14))
        #------------------------------------------
        self.ventana.mainloop()

    def JuegoNuevo(self):
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
                self.Texto1.set("¡Felicidades Has ganado! :) ")
                self.Texto2.set("La palabra es "+self.ObjetoJuego.getPalabra())
            else:
                self.Texto1.set("Lo siento, perdiste :( ")
                self.Texto2.set("La palabra era "+self.ObjetoJuego.getPalabra())
        self.__Dibujo()        

    def __Dibujo(self):
        if self.EstamosJugando:
            oportunidades=self.ObjetoJuego.getOportunidades()
            if oportunidades==1:
                self.Lienzo.delete("all")
                self.Lienzo.create_line(40,280,40,30,150,30,150,70,width=5,fill="white")#horca
                self.Lienzo.create_line(20,290,20,280,280,280,280,290,width=5,fill="white")#horca
                self.Lienzo.create_oval(130,70,170,110,width=5,fill="dark green",outline="white")#cabeza
                self.Lienzo.create_line(150,110,150,190,width=5,fill="white")#torso
                self.Lienzo.create_line(150,120,110,180,width=5,fill="white")#brazo1
                self.Lienzo.create_line(150,120,190,180,width=5,fill="white")#brazo2
                self.Lienzo.create_line(150,190,110,250,width=5,fill="white")#pierna1
            elif oportunidades==2:
                self.Lienzo.delete("all")
                self.Lienzo.create_line(40,280,40,30,150,30,150,70,width=5,fill="white")#horca
                self.Lienzo.create_line(20,290,20,280,280,280,280,290,width=5,fill="white")#horca
                self.Lienzo.create_oval(130,70,170,110,width=5,fill="dark green",outline="white")#cabeza
                self.Lienzo.create_line(150,110,150,190,width=5,fill="white")#torso
                self.Lienzo.create_line(150,120,110,180,width=5,fill="white")#brazo1
                self.Lienzo.create_line(150,120,190,180,width=5,fill="white")#brazo2
            elif oportunidades==3:
                self.Lienzo.delete("all")
                self.Lienzo.create_line(40,280,40,30,150,30,150,70,width=5,fill="white")#horca
                self.Lienzo.create_line(20,290,20,280,280,280,280,290,width=5,fill="white")#horca
                self.Lienzo.create_oval(130,70,170,110,width=5,fill="dark green",outline="white")#cabeza
                self.Lienzo.create_line(150,110,150,190,width=5,fill="white")#torso
                self.Lienzo.create_line(150,120,110,180,width=5,fill="white")#brazo1
            elif oportunidades==4:
                self.Lienzo.delete("all")
                self.Lienzo.create_line(40,280,40,30,150,30,150,70,width=5,fill="white")#horca
                self.Lienzo.create_line(20,290,20,280,280,280,280,290,width=5,fill="white")#horca
                self.Lienzo.create_oval(130,70,170,110,width=5,fill="dark green",outline="white")#cabeza
                self.Lienzo.create_line(150,110,150,190,width=5,fill="white")#torso
            elif oportunidades==5:
                self.Lienzo.delete("all")
                self.Lienzo.create_line(40,280,40,30,150,30,150,70,width=5,fill="white")#horca
                self.Lienzo.create_line(20,290,20,280,280,280,280,290,width=5,fill="white")#horca
                self.Lienzo.create_oval(130,70,170,110,width=5,fill="dark green",outline="white")#cabeza
            else:
                self.Lienzo.delete("all")
                self.Lienzo.create_line(40,280,40,30,150,30,150,70,width=5,fill="white")#horca
                self.Lienzo.create_line(20,290,20,280,280,280,280,290,width=5,fill="white")#horca
 
        else:
            if self.ObjetoJuego.getVictoria():
                self.Lienzo.delete("all")
                self.Lienzo.create_oval(130,70,170,110,width=5,fill="dark green",outline="white")#cabeza
                self.Lienzo.create_line(150,110,150,190,width=5,fill="white")#torso
                self.Lienzo.create_line(150,130,100,80,width=5,fill="white")#brazo1
                self.Lienzo.create_line(150,130,200,80,width=5,fill="white")#brazo2
                self.Lienzo.create_line(150,190,110,250,width=5,fill="white")#pierna1
                self.Lienzo.create_line(150,190,190,250,width=5,fill="white")#pierna2
            else:
                self.Lienzo.delete("all")
                self.Lienzo.create_line(40,280,40,30,150,30,150,70,width=5,fill="white")#horca
                self.Lienzo.create_line(20,290,20,280,280,280,280,290,width=5,fill="white")#horca
                self.Lienzo.create_oval(130,70,170,110,width=5,fill="dark green",outline="white")#cabeza
                self.Lienzo.create_line(150,110,150,190,width=5,fill="white")#torso
                self.Lienzo.create_line(150,120,110,180,width=5,fill="white")#brazo1
                self.Lienzo.create_line(150,120,190,180,width=5,fill="white")#brazo2
                self.Lienzo.create_line(150,190,110,250,width=5,fill="white")#pierna1
                self.Lienzo.create_line(150,190,190,250,width=5,fill="white")#pierna2



if __name__=="__main__":a=JuegoTk()
