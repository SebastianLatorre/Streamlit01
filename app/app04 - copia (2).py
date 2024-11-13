import pandas as pd
import streamlit as st
import numpy as np
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf



# Configuramos la pagina de Streamlit
st.set_page_config(page_title="Dashboard Piscicultura",
                   page_icon="imagen.png",
                   layout="centered",
                   initial_sidebar_state="auto")

# Definimos el titulo y la descripcion de la aplicacion
st.title("Dashboard Planta Piscicultura")
st.markdown("""En esta pagina web simulamos una Planta Acuicola""")
st.markdown("""---""")

# Cargamos y mostramos el logo en la barra laterial
logo = "imagen2.png"
st.sidebar.image(logo, width=600)

# Añadimos un encabezado para la seccion de datos del usuario en la barra lateral
st.sidebar.header("Datos ingresados por el usuario")

# Función para capturar los datos del usuario
def user_input_features():
    sbp = st.sidebar.slider("Presion arterial (mmHg)", 101, 218, 150)
    tobacco = st.sidebar.slider("Tabaco Acumulado (Kg)", 0.00, 31.20, 2.00)
    ldl = st.sidebar.slider("Colesterol de Lipoproteinas de Baja Densidad (mg/dL)", 0.98, 15.33, 4.34)
    adiposity = st.sidebar.slider("Adiposidad (Adimencional)", 6.74, 42.49, 26.12)
    famhist = st.sidebar.selectbox("Antecedentes Familiares de Enfermedad Cardiaca (Presente / Ausente)", ("Present", "Absent"))
    typea = st.sidebar.slider("Tipo (Adimencional)", 13, 78, 53)
    obesity = st.sidebar.slider("Obesidad (IMC)", 14.70, 46.58, 25.80)
    alcohol = st.sidebar.slider("Alcohol (UBE)", 0.00, 147.19, 25.00)
    age = st.sidebar.slider("Edad (Años)", 15, 64, 45)

    # Creamos un diccionario con los datos ingresados por el usuario
    data = {
        "sbp": sbp,
        "tobacco": tobacco,
        "ldl": ldl,
        "adiposity": adiposity,
        "famhist": famhist,
        "typea": typea,
        "obesity": obesity,
        "alcohol": alcohol,
        "age": age
    }

    # Convertimos el diccionario en un DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Capturamos los datos del usuario
input_df = user_input_features()

# Aplicamos LabelEncoder para convertir los valores de antecedentes familiares (Present, Absent)
input_df['famhist'] = input_df['famhist'].map({'Present': 1, 'Absent': 0})

# Mostramos los datos ingresados por el usuario
st.subheader("Datos ingresados por el usuario")
st.write(input_df)

# Cargamos el modelo de TensorFlow
model = tf.keras.models.load_model('assets/model.keras')

# Función para predecir usando el modelo cargado
@st.cache_resource
def predict(input_df):
    prediction = model.predict(input_df)
    return prediction

col1, col2 = st.columns(2)

# Generar la prediccion
with col1:
    st.subheader("Resultados del modelo")
    prediction = predict(input_df)
    st.write('Predicción:', prediction)

if prediction[0] > 0.5:
    prediction_text = "Alta probabilidad de tener problemas cardíacos, favor volver a revisar la información ingresada"
    prediction_color = "red"
else:
    prediction_text = "La persona no tiene problemas cardíacos"
    prediction_color = "green"

with col2:
    st.subheader("Resultados")
    st.markdown(f'<h2 style="color:{prediction_color};">{prediction_text}</h2>', unsafe_allow_html=True)
    st.markdown("""---""")

#poetry run streamlit run app04.py
