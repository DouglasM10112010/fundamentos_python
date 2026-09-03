#Autor: Douglas Magalhães 
# Projeto: Uso de API (conceito de dicionario)

#requisições http - GET
import requests

#Uso da API no ViaCEP

piloto = input('Numero do piloto: ')

url= f"https://api.openf1.org/v1/drivers?driver_number={piloto}&session_key=9158"
resposta = requests.get(url)
dados = resposta.json()

print(f"Nome do piloto: {dados[0]['full_name']}")

