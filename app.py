import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Tabela Interativa de Veículos')

df_vehicles = pd.read_csv('vehicles.csv')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write(
        'Histograma comparativo de preços e ano dos modelos')

    fig = px.histogram(df_vehicles, y="price", x="model_year")

    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')

# outro grafico de barras(selecionando o veículo e apresentando o valor)

st.title("Preços de Veículos")

selected_type = st.selectbox(
    "Que tipo de veículo você procura?", df_vehicles['type'].unique())

filtered_data = df_vehicles[df_vehicles['type'] == selected_type]

fig = px.bar(filtered_data, x="model", y="price", color="model",
             title="Preços por Modelo de Veículo")
st.plotly_chart(fig)

# gráfico de dispersão: estado x ano veiculo
st.title("Condições do veículo pelo ano")

fig = px.scatter(df_vehicles, x='odometer', y='condition',
                 color='condition', title='Condições pela Quilometragem')
st.plotly_chart(fig)
