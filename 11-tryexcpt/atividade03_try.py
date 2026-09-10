#Douglas Magalhães
#Projeto: Try Except
#try: código sem exeção
#except: tratamento de exeção
def divisao():
    try:
        valor1 = float(input('digite o primeiro valor: '))
        valor2 = float(input('digite o segundo valor: '))
        divisao = valor1 / valor2
    except ZeroDivisionError:
        print('Não é possivel fazer a divisão por 0')
    except ValueError:
        print("Caro usuario, você não digitou um número")
        print("---------------Digite um número---------------")
    else:
        print(f"O resultado da divisão é: {divisao:.2f}")
divisao()
