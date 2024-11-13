FROM python:3.9

# Actualizar pip
RUN pip install pip --upgrade
# Instalar Poetry (especificando versión)
RUN pip install poetry==1.8.3

# Indica la carpeta del contenedor en la que
# se ejecutarán los comandos posteriores
WORKDIR /app04

# Copiar archivos de Poetry
COPY pyproject.toml ./pyproject.toml
COPY poetry.lock ./poetry.lock

# Instalar dependencias con Poetry
RUN poetry install

# Copiar archivos del proyecto
COPY . .
# COPY app.py ./app.py
# COPY imagen.png ./imagen.png
# COPY assets/model.keras ./assets/model.keras

# Abrir puerto para Streamlit
EXPOSE 8501

# Comando a ejecutar
CMD [ "poetry", "run", "streamlit", "run", "app04.py", "--server.port=8501", "--server.address=0.0.0.0" ]
