from PalabraNueva import PalabraNueva

class ClaseJuego:

    def __init__(self):
        self.nuevojuego()
        
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
        self.LetrasNecesarias=[]
        for letra in self.palabraDeletreada:
            if letra!=" ":
                if not(letra in self.LetrasNecesarias): self.LetrasNecesarias.append(letra)
        self.LetrasAdivinadas=[]
        self.victoria=False        

    def getPalabra(self): return self.palabra
    def getLetrero(self): return self.letreroJuego
    def getLetrasUsadas(self): return self.LetrasUsadas
    def getOportunidades(self): return self.oportunidades
    def getJugadorEstaVivo(self): return self.JugadorEstaVivo
    def getLetrasNecesarias(self): return self.LetrasNecesarias
    def getLetrasAdivinadas(self): return self.LetrasAdivinadas
    def getVictoria(self): return self.victoria

    def jugar(self,jugada):
        try:jugada=str(jugada).lstrip()[0].upper()
        except: jugada=" "
        if jugada.isalpha() or jugada=="Ñ":
            #print("jugada correcta "+jugada)
            if not(jugada in self.LetrasUsadas):
                self.LetrasUsadas.append(jugada)
                if jugada in self.LetrasNecesarias: #acierto
                    self.LetrasAdivinadas.append(jugada)
                    self.__ActualizarLetrero()
                    if len(self.LetrasAdivinadas)==len(self.LetrasNecesarias):self.victoria=True
                else:
                    self.oportunidades-=1 #error
                    if not(self.oportunidades):self.JugadorEstaVivo=False
                return True
            else: return False
        else: return False

    def __ActualizarLetrero(self):
        self.letreroJuego.clear()
        for letra in self.palabraDeletreada:
            if letra in self.LetrasAdivinadas:self.letreroJuego.append(letra)
            elif letra.isspace():self.letreroJuego.append(" ")
            else: self.letreroJuego.append("_")

if __name__=="__main__":
    j=ClaseJuego()
    print(j.getPalabra())
    j.jugar(" A")
    j.jugar("E")
    j.jugar("Ñ")
    j.jugar("   123")
    j.jugar(" /(&(/!")
    j.jugar(" uio 987987 8")
    j.jugar("")

