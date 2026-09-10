#Autor: Douglas Magalhães
#Projeto: Salvar dados em arquivo TXT

nome = input("Digite seu nome: ")
cel = input("digite seu numero: ")

arquivo = open("arquivo.txt", "a")
arquivo.write(nome + " | " + cel + "\n")
arquivo.close()

