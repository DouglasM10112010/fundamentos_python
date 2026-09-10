#Douglas Magalhães
#Projeto: Tratamento de conta IMC 

def imc():
    try:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        nome = input("Digite o seu nome: ")
        resposta = peso / altura**2
    except ZeroDivisionError:
        print("Não pode ser dividido por zero 0!")
    except ValueError:
        print("Não é aceitavel letras")
    else:
        if resposta <= 18.5:
            print("Você esta muito magro, cuidado")
        elif resposta <= 25:
            print("Você está saldavel")
        elif resposta <= 30:
            print("Você está sobre peso, cuidado!")
        else:
            print("Cuidado, você está obeso")
        print(f"Seu IMC é: {resposta:.1f}")
        arquivo = open("IMCs.txt", "a")
        arquivo.write(f"{nome} | {resposta:.1f}\n")
        arquivo.close()
        print("Seu dado foi colocado no arquivo IMCs.txt")
imc()


        