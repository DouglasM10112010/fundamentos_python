#Autor: Douglas Magalhães de B. F.
#Projeto: Listas

#lista de frutas com 5 unidades
#             0        1        2          3        4
frutas = ['banana', 'maça', 'abacaxi', 'goiaba', 'kiwi']

print(frutas)

#Adição de um item na lista
frutas.append('laraja')
print(frutas)

# Alterar o conteudo de uma possição
# Mudar a fruta Kiwi para Morango
frutas[4] = 'morango'
print(frutas)

# Deletar um item por posição
# exclusão da maça
del frutas[1]
print(frutas)
#Inserir uma nova fruta na posição 1
frutas.insert(1,'mamão')
print(frutas)

# Ordena a lista
frutas.sort()
print(frutas)
