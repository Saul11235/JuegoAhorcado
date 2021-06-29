from PalabraNueva import PalabraNueva

class ClaseJuego:

    def __init__(self):
        self.nuevojuego()
        print(self.palabra)
        
    def nuevojuego(self):
        self.palabra=PalabraNueva()
        self.palabraDeletreada=[]
        for letra in self.palabra:self.palabraDeletreada.append(letra)
        self.letreroJuego=[]
        for letra in self.palabraDeletreada:
            if letra==" ":self.letreroJuego.append(" ")
            else:self.letreroJuego.append("_")
        self.LetrasUsadas=[]
        self.oportunidades=6
        self.JugadorEstaVivo=True




if __name__=="__main__":
    j=ClaseJuego()

