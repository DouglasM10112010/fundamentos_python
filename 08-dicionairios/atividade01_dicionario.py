#Autor: Douglas Magalhães 
# Projeto: Dicionarios

#projeto "aquele lá"
escola = {
    "salas": "sala_musica",
    "localizacao": "bloco_A",
    "qtd_lugares": "40",
    "caracteristica": "acustica"
}

#acessando dados do dicionario
print(f'Sala disponivel {escola["salas"]}')

# Adicionando mais itens ao dicionario
escola["iluminacao"] = "led"
print(f'iluminação da sala {escola["iluminacao"]}')

#Alterando o valor do dicionario
escola["sala"] = "sala"
print(f'tipo do local: {escola["sala"]}')