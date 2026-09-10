#Douglas Magalhães
#Projeto: Try Except
#try: código sem exeção
#except: tratamento de exeção

try:
    valor1 = float(input('digite o primeiro valor: '))
    valor2 = float(input('digite o segundo valor: '))
    soma = valor1 + valor2
    print(f"O resultado da soma é: {soma}")
except:
    print("Caro usuario, você não digitou um número")
    print("---------------Digite um número---------------")
    