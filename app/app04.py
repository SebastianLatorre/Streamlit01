# import boto3
# import pandas as pd
# from botocore.exceptions import NoCredentialsError

# # Usa el perfil 'default' o el que prefieras
# session = boto3.Session(profile_name="default")  # Cambia el nombre del perfil si es necesario
# s3 = session.client('s3')

# bucket_name = "patagoniacontrol-monitoring-data"
# file_key = "iot_data.csv"

# def load_data_from_s3(bucket_name, file_key):
#     try:
#         response = s3.get_object(Bucket=bucket_name, Key=file_key)
#         data = pd.read_csv(response['Body'])
#         return data
#     except NoCredentialsError:
#         print("Credenciales no válidas")
#         return None

# # Llama a la función para cargar los datos
# data = load_data_from_s3(bucket_name, file_key)

# if data is not None:
#     print(data.head())  # Muestra las primeras filas para verificar


import streamlit as st
import pandas as pd
import boto3
import plotly.express as px
import altair as alt
from botocore.exceptions import NoCredentialsError

# Configuración de AWS
session = boto3.Session(profile_name="default")  # Cambiar el perfil si es necesario
s3 = session.client('s3')

bucket_name = "patagoniacontrol-monitoring-data"
file_key = "iot_data.csv"

def load_data_from_s3(bucket_name, file_key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        data = pd.read_csv(response['Body'])
        return data
    except NoCredentialsError:
        print("Credenciales no válidas")
        return None

# Cargar los datos de S3
data = load_data_from_s3(bucket_name, file_key)

if data is not None:
    st.title("Gráficos Interactivos con Plotly y Altair")
    
    # Visualizar las primeras filas
    st.subheader("Primeras filas de los datos")
    st.write(data.head())

    # Convertir la columna 'time' a tipo datetime, extrayendo la parte correcta
    data['time'] = pd.to_datetime(data['time'].str.split(' UTC').str[0], errors='coerce')
    
    # Verificar si la conversión fue exitosa
    if data['time'].isnull().any():
        st.warning("Algunos valores de 'time' no se pudieron convertir correctamente.")
    
    # Graficar con Plotly (temperatura vs tiempo)
    st.subheader("Temperatura a lo largo del tiempo")
    fig = px.line(data, x='time', y='temperature', title='Temperatura a lo largo del tiempo')
    st.plotly_chart(fig)
    
    # Graficar con Altair (dispersión de nitratos vs temperatura)
    st.subheader("Relación entre Nitratos y Temperatura")
    chart = alt.Chart(data).mark_circle(size=60).encode(
        x='nitrates',
        y='temperature',
        color='salinity',
        tooltip=['nitrates', 'temperature', 'salinity']
    ).properties(
        title='Relación entre Nitratos y Temperatura'
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.error("No se pudieron cargar los datos desde S3.")


