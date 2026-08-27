#Autor: Douglas Magalhães
#Projeto: site de imc

import streamlit as st

#Titulo da pag
st.title('Calculadora de imc')

#entrada de dados
peso = st.number_input('peso (Kg): ')
altura = st.number_input('autura (m): ')

#botão com ação de caucular e stats
if st.button('Caucular IMC'):
    imc = peso/(altura**2)
    st.success(f'Seu IMC é: {imc:.2f}')

    #condicional da resposta
    if imc < 18.5:
        st.warning('Abaixo do peso')
    elif imc < 20.0:
        st.success('peso comum')
    elif imc < 30.0:
        st.warning('sobrepeso')
    else:
        st.error('Obesidade')