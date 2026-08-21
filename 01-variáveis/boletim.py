#Autor: Douglas Magalhães
#Projeto: Utilizado if/elif/else

#definição das variaveis
nota1 = float(input('Digite a 1ªnota: '))
nota2 = float(input('Digite a 2ªnota: '))
media = (nota1 + nota2) / 2
print(f'Sua média é: {media:.1f}') # :.xf formata para duas casas decimais

#Estrutura condicional
#Se a media for maior ou igual a 7; Aluno aprovado
#Se a media for menor a 7; Aluno reprovado
if media >= 7:
    # \n serve para pular uma linha
    print('Aluno aprovado \n😊👍')
else:
    print('Aluno reprovado \n😢😞')