from ClaseJuego import ClaseJuego
from os import system

class JuegoModoConsola:

    def __init__(self):
        self.juego=ClaseJuego()
        self.EstamosJugando=False
        self.EntradaConsola=""
        self.PrimerJuego=True
        while True:
            if self.EstamosJugando: self.__pantallazoEnJuego()
            else: self.__pantallazoEnEspera()
            self.EntradaConsola=input(" >>> ")
            system("cls") #cls-Windows   clear-Linux Mac
            if self.EstamosJugando:
                self.juego.jugar(self.EntradaConsola)
                if self.juego.getVictoria() or not(self.juego.getJugadorEstaVivo()):
                    self.EstamosJugando=False
            else:
                if self.EntradaConsola.strip()=="":
                    self.EstamosJugando=True
                    self.PrimerJuego=False
                    self.juego.nuevojuego()
                else: exit()    
        
    def __pantallazoEnEspera(self):
        if self.PrimerJuego:print("\n\nJuego del Ahorcado por ESPM")
        else:
            if self.juego.getJugadorEstaVivo():
                print("\n\n\n     \   /\n      \O/\n       |  \n       |   \n      / \ \n     /   \  ")
                print("\n\nFelicitaciones\nLa palabra era : "+str(self.juego.getPalabra()))
            else:
                print("\n XXX\n XXX---+\n XXX   |\n       O\n      /|\ \n     / | \ \n      / \ \n     /   \  ")
                print("\n\nLo siento, perdiste :( \nLa palabra era : "+str(self.juego.getPalabra()))
        print("\nPara continuar sólo presiona enter, ingresa otro valor para salir...\n")
    
    def __pantallazoEnJuego(self):
        oportunidades=self.juego.getOportunidades()
        if   oportunidades==1:print("\n XXX\n XXX---+\n XXX   |\n       O\n      /|\ \n     / | \ \n      /   \n     /      ")
        elif oportunidades==2:print("\n XXX\n XXX---+\n XXX   |\n       O\n      /|\ \n     / | \ \n          \n            ")
        elif oportunidades==3:print("\n XXX\n XXX---+\n XXX   |\n       O\n      /|  \n     / |   \n          \n            ")
        elif oportunidades==4:print("\n XXX\n XXX---+\n XXX   |\n       O\n       |  \n       |   \n          \n            ")
        elif oportunidades==5:print("\n XXX\n XXX---+\n XXX   |\n       O\n          \n           \n          \n            ")
        else:                 print("\n XXX\n XXX---+\n XXX   |\n        \n          \n           \n          \n            ")
        letrero="";TusJugadas=""
        for letra in self.juego.getLetrero():letrero+=letra+" "
        for letra in self.juego.getLetrasUsadas():TusJugadas+=letra
        print("\n\n      "+letrero)
        print("\n\n Tus jugadas: "+TusJugadas+"\n")

if __name__=="__main__":
    j=JuegoModoConsola()
