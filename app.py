import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Análisis de anuncios de venta de carros en EE.UU.')
st.write('Explora la distribución y relaciones en el conjunto de datos de vehículos.')

# --- Histograma ---
st.subheader('Distribución del Odómetro')
hist_button = st.checkbox('Mostrar histograma del odómetro')

if hist_button:
    st.write(
        'Histograma que muestra cuántos carros hay según el kilometraje recorrido.')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Cantidad de vehículos'
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico de dispersión ---
st.subheader('Relación entre Odómetro y Precio')
scatter_button = st.checkbox('Mostrar gráfico de dispersión')

if scatter_button:
    st.write('Gráfico que muestra cómo el kilometraje afecta el precio de venta.')
    fig2 = go.Figure(data=[go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(opacity=0.4)
    )])
    fig2.update_layout(
        title_text='Odómetro vs Precio',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)'
    )
    st.plotly_chart(fig2, use_container_width=True)
