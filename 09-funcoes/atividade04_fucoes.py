#Autor: Douglas Magalhaes
#Projeto: fuções dentro de fuções

#juros siples j = C * i * t 
#montante M = C + J
def calcular ():
    def jurus_simples(c, i, t):
        return c * i * t

#juros compostos J = M - C
#montante M = C * (i + 1)^t
    def juros_compostos(c, i, t,):
        return c*(1+i)**t - c

    #Alternativas
    op = input("selecione juros: 1 = simples; 2 = compostos: ")

    #entrada de dados
    c = float(input("Digite o capital: "))
    i = float(input("Digite a taxa (decimal): "))
    t = float(input("Digite as parcelas: "))

    # Condicionais que escolhem a operação
    if op == 1:
        print(jurus_simples(c, i, t))
    else:
        print(juros_compostos(c, i, t))


calcular()