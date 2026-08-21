#Autor: Douglas Magalhães
#Projeto: Utilizado if/elif/else
#Operadores de comparação
# == igual
# !< diferente
# 
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
elif media <= 4:
    print('Aluno reprovado \n😢😞')
else:
    print("Aluno em recuperação \n😑🤨")