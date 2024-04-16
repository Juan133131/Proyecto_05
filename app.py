import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Proyecto Sprint 5: ddddd ')
st.write('Prueba: Juan Villano')


st.write('Esta es un anális de: ') 


hist_checkbox = st.checkbox('Histograma de millaje de vehiculos', key= 'his_checkbox') # crear un botón
scatter_checkbox = st.checkbox('Diagrama de dispersion de precio vs millaje', key= 'scatter_checkbox')       

#Verificar que la casilla de verificacion este seleccionada

if hist_checkbox:
    #crear un histograma
    fig = px.histogram(car_data, x='odometer', title='Histograma de millaje de vehiculos')
    #Mostrar un grafico ploty interctivo
    st.plotly_chart(fig, use_container_width=True)
    #Escribir mensaje
    st.write('Acontinuacion algunas estadisticas descriptivas sobre la variable millaje de los vehiculos')
    #Calcular y mostrar la media, la mediana y la desviacion estandar
    st.write(f"Media: {car_data['odometer'].mean():,.0f}, "
             f"Mediana: {car_data['odometer'].median():,.0f}, "
             f"Desviacion estandar: {car_data['odometer'].std():,.0f}")
    
if scatter_checkbox:
    #crear un grafico de dispersion con plotly Express
    fig2 = px.scatter(car_data, x='odometer', y= 'price', title='Diagrama de dispersion de precio vs millaje')
    #Mostrar un grafico usando st.plotly_chart()
    st.plotly_chart(fig2, use_container_width=True)
    #Escribir mensaje
    st.write('Precio y millaje se encuentran inversamente correlacionados.')
    #Calcular coeficiente de correlacion y mostrar con 3 decimales
    correlation = car_data['odometer'].corr(car_data['price'])
    st.write(f"Coeficiente de correlación: {correlation:.3f}")