import os
import pandas as pd 
import streamlit as st
import time
import torch

from simpletransformers.classification import MultiLabelClassificationModel

from Scripts.tratador_texto import TrataTexto

PATH_PESO = "./Pesos/bert_multicass"

# argumentos do modelo
args = {
    'reprocess_input_data': True,
    'overwrite_output_dir': True,
    'evaluate_during_training': True,
    'use_multiprocessing': False,
    "num_train_epochs": 1,
    "train_batch_size": 16,
    "eval_batch_size": 16,
    'no_cache': True
}

# verificando disponibilidade do cuda
cuda_available = torch.cuda.is_available()
print(cuda_available)

# importando o modelo
model_vencedor = MultiLabelClassificationModel('bert',
                                               PATH_PESO,
                                               args=args,
                                               use_cuda=False)
print(model_vencedor)
tratador = TrataTexto()

st.title("Classificação Multi-label com BERT 💻")

st.text("O dataset utilizado é um dataset de perguntas do Stack Overflow.")
st.markdown("[StackOverflow](https://stackoverflow.com/)")

st.subheader('Insira aqui sua pergunta à ser classificada 🙋:')

pergunta_padrao = "Vi esse vídeo (link abaixo) e gostaria de construir um elemento que somente aparecesse quando a rolagem atingir o 'ponto que toque nele'. Creio que deve ser javascript. Se alguém souber ficaria muito grato :D Tentei linkar os arquivos e add a div no meu projeto mas ela simplesmente sumiu.  OBS: Ele mostra o efeito em 3:46  https://www.youtube.com/watch?v=tdgDr_icGdo"

message = st.text_area('Temos uma pergunta para testes:', pergunta_padrao)

html_page = """
<div style="background-color:tomato; padding:5px">
    <p style="font-size:30px; text-align:center">Resultados</p>
</div>
"""

if st.button("Enviar"):
    st.success("A pergunta recebida será classificada!")
    time.sleep(1)

    st.markdown(html_page, unsafe_allow_html=True)

    try:
        texto_tratado = tratador.fix_text(message)
        predictions, probs = model_vencedor.predict([texto_tratado])

        df_data = [
            [predictions[0][0], probs[0][0], 'NodeJs'],
            [predictions[0][1], probs[0][1], 'Jquery'],
            [predictions[0][2], probs[0][2], 'Html'],
            [predictions[0][3], probs[0][3], 'Angular']
        ]

        st.text('')
        df = pd.DataFrame(df_data)
        df.columns = ["Predição", "Probabilidade", "Label"]
        st.dataframe(df)

    except Exception as error:
        st.text('')
        st.exception(error)