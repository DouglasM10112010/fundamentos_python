#Autor: Douglas Magalhaes
#Projeto: trabalhando com fuções

'''
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('digite o segundo valor: '))
operacao = input('digite a operação (+, -, *, /)')
soma = valor1 + valor2
subitracao = valor1 - valor2
mutiplicacao = valor1 * valor2
divisao = valor1 / valor2
print(f'O valor da soma é: {operacao:.2f}')
'''

def calc_basica(v1, v2, operacao):
    if operacao == "+":
        return v1 + v2
    
    elif operacao == "-":
        return v1 - v2
    
    elif operacao == "*":
        return v1 * v2
    
    elif operacao == "/":
        return v1 / v2
    
    else:
        return 'operação invalida!'


valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação (+, -, *, /): ")
resultado = calc_basica(valor1, valor2, operacao)
print(f"Resultado: {resultado:.2f}")


