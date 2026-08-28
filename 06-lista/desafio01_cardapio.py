#Autor: Douglas Magalhães
#Projeto: Cardapio

#cardapio
nome = input('qual é seu nome? ')
cardapio = ['pizzaiolo', 'muçarela', 'portuguesa', 'calabresa']
print(cardapio)
pedido = [input('incira seu pedido: ')]
pergunta = input('deseja mais alguma coisa: ')

while pergunta != 'não':
    cardapio = ['pizzaiolo', 'muçarela', 'portuguesa', 'calabresa']
    print(cardapio)
    pedido.append(input('incira seu pedido: '))
    pergunta = input('deseja mais alguma coisa: ')

print(f'{nome}, seu pedido foi {pedido}')


    

