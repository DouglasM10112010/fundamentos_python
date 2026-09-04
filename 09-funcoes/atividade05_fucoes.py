#Autor: Douglas Magalhaes
#Projeto: Função converção de real x dolar

def converção(): 
    def dolar(r, d):
        return r / d
    r = float(input("valor dos reais: "))
    d = float(input("valor dos dolar: "))
print(f"U${converção()}")
