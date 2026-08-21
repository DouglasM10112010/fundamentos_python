#Autor: Douglas Magalhães
#Projeto: Motorista if/else | and | variaveis

nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade'))
carteira = True

#Estrutura condicional
#'and' todas as condições tem que ser verdadeiras
if idade >= 18 and carteira:
    print(f'{nome}, Autorizado a Dirigir')
else:
    print(f'{nome}, Não autorisado a Dirigir')

