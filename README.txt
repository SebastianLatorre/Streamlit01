----------------------- Streamlit -------------------------------

-> Instrucciones que solo se utilizan para correr por primera vez

pyenv install 3.9.0
pyenv local 3.9.0
poetry env use 3.9.0
poetry update

-> Para abrir el streamlit

poetry run Streamlit run app04.py



----------------------- Docker ----------------------------------

-> Contruir la imagen
docker build --tag imagen-con-poetry .

-> Ejecutrar el contenedor de docker
docker run --name contenedor-con-poetry --publish 8501:8501 imagen-con-poetry

-> Ahora podemos acceder a la aplicación en
http://127.0.0.1:8501


--> Para ejecutar en segundo plano
docker run --name contenedor-con-poetry --detach --publish 8501:8501 imagen-con-poetry