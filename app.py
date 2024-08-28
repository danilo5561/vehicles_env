import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Interactive Vehicle Table')
# lendo os dados
csv = r'C:\Users\User\vehicles.csv'
df_vehicles = pd.read_csv(csv)

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    fig = px.histogram(df_vehicles, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
  st.write('Criando um histograma para a coluna odometer')