#Autor: Douglas Magalhaes
#Projeto: Função converção de real x dolar p2
import requests

valor = float(input("U$: ").strip())

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
resposta = requests.get(url)
dados = resposta.json()

cotacao= float(dados["USDBRL"]["bid"])
convertido = valor * cotacao

print(f"O valor é R${convertido:.2f}")