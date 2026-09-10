#Douglas Magalhães
#Projeto: Try Except
#try: código sem exeção
#except: tratamento de exeção

try:
    valor1 = float(input('digite o primeiro valor: '))
    valor2 = float(input('digite o segundo valor: '))
    divisao = valor1 / valor2
    print(f"O resultado da divisão é: {divisao:.2f}")
except ZeroDivisionError:
    print('Não é possivel fazer a divisão por 0')
except ValueError:
    print("Caro usuario, você não digitou um número")
    print("---------------Digite um número---------------")
        