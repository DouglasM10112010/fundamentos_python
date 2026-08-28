#Autor: Douglas Magalhães
#Projeto: Loop While

tabuada = int(input('Qual é a tabuada desejada'))
i = 1
while i <= 10:
    print(f'{tabuada} x {i} = {tabuada * i}')
    i = i + 1
#   i+=1

# i=1 <=10 (sim!)
#              2 x i (1) = 2
#              i = i + 1 = (1+1=2)
# print(f'{tabuada} x {i} = {tabuada * i}')
# i = i+1