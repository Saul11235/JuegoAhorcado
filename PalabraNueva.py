from random import choice 

ArchivoExterno=open("PALABRAS","r")
ListaPalabras=[]

for palabra in ArchivoExterno:
    PalabraCorregida=palabra.upper().removesuffix("\n")
    if PalabraCorregida!="":ListaPalabras.append(PalabraCorregida)

def PalabraNueva():
    try: return(choice(ListaPalabras))
    except:return("PALABRAS")

if __name__=="__main__":
    print(PalabraNueva())
