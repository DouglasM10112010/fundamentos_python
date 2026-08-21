import streamlit as st

#Titulo da página
st.title('calculadora de IMC')

#Texto explicativo
st.write('my firts pag')

#Input de dados
nome = st.text_input('digite seu nome: ')

#Botão
if st.button('Enviar'):
    if nome:
        st.success(f'Olá {nome}, Seja bem vindo!')
    else:
        st.warning('Gentileza, digitar seu nome')