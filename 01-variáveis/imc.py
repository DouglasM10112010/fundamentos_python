#Autor: Douglas Magalhães
#Projeto: Calculadora de IMC

print('========= CALCULADORA DE IMC ==========')
peso = float(input('digite seu peso (Kg): '))
altura = float(input('digite sua altura (M): '))
imc = peso / (altura * altura)
print(f'Seu IMC é: {imc:.2F}')

# Estrutura condicional
if imc <= 18.5:
    print('Cuidado! Magreza!🚨')
elif imc <= 25.0:
    print('Parabéns! Saudavel!')
elif imc <= 30.0:
    print('Ateção! Sobrepeso!')
elif imc <= 35.0:
    print('Se cuide direito! Obeso grau 1ª')
elif imc <= 40.0:
    print('Se cuide direito! Obeso grau 2ª')
else:
    print('Se cuide direito! Obeso grau 3ª')   