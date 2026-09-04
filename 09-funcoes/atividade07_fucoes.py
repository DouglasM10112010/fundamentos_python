#Autor: Douglas Magalhães
#Projeto: convertor de Dolar x Real p3

def converso():
    def calc (valor, url, resposta, cotacao, convertido, dados):
        import requests

       
        url = "https://economia.awesomeapi.com.br/last/USD-BRL"
        resposta = requests.get(url)
        dados = resposta.json()

        cotacao= float(dados["USDBRL"]["bid"])
        convertido = valor * cotacao
        valor = float(input("U$: ").strip())

        print(f"O valor é R${convertido:.2f}")

converso()