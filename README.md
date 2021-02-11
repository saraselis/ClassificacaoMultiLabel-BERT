<h1 align="center">ClassificacaoMultiLabel-BERT 👋</h1>
<p>
</p>

# Projeto :bomb:
O projeto foi pensado para resolver o problema de classificação multi-label de perguntas retiradas do site Stack Overflow. As perguntas podem ser classificadas como **node.js**, **jquery**, **html** e **angular**. Uma mesma pergunta pode haver apenas uma label ou até mesmo todas as labels.

![Tags](https://github.com/saraselis/ClassificacaoMultiLabel-BERT/blob/main/Files/tags.jpeg)

O classificador selecionado para tentar resolver esse problema, foi a implementação BERT do **[simpletransformers](https://simpletransformers.ai/docs/usage/)**. A biblioteca em questão foi escolhida devido a sua praticidade de implementação e os bons resultados obtidos mesmo com poucas amostras disponíveis. Além disso, o framework agiliza algumas etapas de pré-processamento textual. 

> Status do Projeto: em andamento :grey_exclamation:

## Pré-requisitos :question:
1. Para rodar o projeto em um container [Docker](https://www.docker.com/):

`bash build.sh`

`bash run.sh`

Posteriormente, basta acessar a url `http://172.17.0.2:8501`.

2. Para rodar o projeto localmente, basta criar um novo ambiente de trabalho [Anaconda](https://docs.anaconda.com).
Dentro do diretório <i>Files</i> encontra-se o arquivo yml referênte ao ambiente utilizado no desenvolvimento do projeto.

`conda env create -f environment.yml`

`conda activate BertMultilabel`

Logo após, será necessário rodar o script **app.py**.

`streamlit run app.py`

## Executando :running:
A API será executada com [Streamlit](https://www.streamlit.io/).

Os notebooks de estudos e treinamentos estão no diretório `/Jupyters`.

## Testando :books:
Para realizar o teste de predição, basta colocar a pergunta em questão na caixa de texto e clicar em <i>Enviar</i>.
A pergunta será pré-processada e classificada.

![Imagem](https://github.com/saraselis/ClassificacaoMultiLabel-BERT/blob/main/Files/front.jpeg)


## Melhorias :trophy:
- [ ] Testar algorítimos OnevsRest
- [ ] Testar algorítimos adaptados


<p align="justify"> </p> <img src="https://img.shields.io/static/v1?label=Python&message=Bert&color=brightgreengreen&style=for-the-badge&logo=Python"/>

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
