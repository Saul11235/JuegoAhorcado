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
                try: self.LetrasNecesarias.index(letra)
                except: self.LetrasNecesarias.append(letra)
        self.LetrasAdivinadas=[]
        self.victoria=False        

    def getPalabra(self): return self.palabra
    def getLetrero(self): return self.letreroJuego
    def getLetrasUsadas(self): return self.LetrasUsadas
    def getOportunidades(self): return self.oportunidades
    def getJugadorEstaVivo(self): return self.JugadorEstaVivo
    def getLetrasNecesarias(self): return self.LetrasNecesarias
    def getVistoria(self): return self.victoria

    def jugar(self,jugada):
        try:jugada=str(jugada).lstrip()[0].upper()
        except: jugada=" "
        if jugada.isalpha() or jugada=="Ñ":
            try:
                self.LetrasUsadas.index(jugada) #except si es letra nueva
                return False
            except:
                self.LetrasUsadas.append(jugada)
                try:
                    self.LetrasNecesarias.index(jugada) #jugada correcta
                    self.LetrasAdivinadas.append(jugada)
                    sel.__ActualizarLetrero()
                    if len(self.LetrasAdivinadas)==len(self.LetrasNecesarias):self.victoria=True
                except:
                    self.oportunidades-=1 #jugada incorrecta
                    if not(self.oportunidades): self.JugadorEstaVivo=False

                    pass

                print("letra nueva")
                return True
        else:
            return False

        def __ActualizarLetrero(self):
            pass
        print(jugada)

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

