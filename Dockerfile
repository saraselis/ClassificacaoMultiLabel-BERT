FROM python:3.7

USER root

# DEPENDENCIAS
    # --- NLTK
COPY ./Files/nltk_data /root/nltk_data
RUN chmod +x -R /root/nltk_data

# INSTANLANDO APLICACAO
COPY . /app 
WORKDIR /app

    # --- INSTALANDO BIBLIOTECAS
RUN pip install -r requirements.txt
EXPOSE 8501

# RODANDO A APLICACAO
ENTRYPOINT ["streamlit","run"]
CMD ["app.py"]