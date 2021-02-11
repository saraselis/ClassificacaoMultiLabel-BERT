import logging
import nltk
import re
import sys

from pyfields import field

remove_accent_ = {'a': r'[\xE0-\xE6]', 'e': r'[\xE8-\xEB]',
                  'i': r'[\xEC-\xEF]',
                  'o': r'[\xF2-\xF6]',
                  'u': r'[\xF9-\xFC]', 'c': r'[\xE7]', 'y': r'[\xFD|\xFF]'}

remove_stop_ = set(nltk.corpus.stopwords.words('portuguese'))

string_pont_ = '[!"#$%&\'()*+-/:;<=>?@[\\]^_`{|}~—"\'“”ª«»£@#$%¢¬&*§º]'

logger = logging.getLogger("BERT Multi-Label")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
formatter = logging.Formatter('%(name)s - %(levelname)s - [+] ------- %(message)s -------') 
handler.setFormatter(formatter)
logger.handlers = [handler]
# nltk.download('stopwords')

class TrataTexto:
    '''
        Classe destinada ao tratamento do texto enviado para
            realização da predição.

        Atributos da classe:
            \t* remove_accent_str - Regex para remoção de acentos
            \t* string_pont - Regex para remoção de pontuação
            \t* remove_stop -  Stopwords NLTK
    '''

    remove_accent_str: str = field(doc="String regex para remoção de acentos.",
                                  default=remove_accent_, check_type=True,
                                  type_hint=dict)
    string_pont: str = field(doc="String regex para remoção de pontos.",
                             default=string_pont_, check_type=True,
                             type_hint=str)
    remove_stop: list = field(doc="Nltk Stopwords.",
                              default=remove_stop_, type_hint=dict)
    count: int = field(doc="Contador para textos", default=1, type_hint=int)

    def remove_accent(self, text: str) -> str:
        """Remove os acentos das palavras do texto.

        :param text: texto
        :type text: str
        :return: texto sem acentos
        :rtype: str
        """

        for letter, regex in self.remove_accent_str.items():
            text = re.sub(regex, letter, text)

        return text

    def remove_pont(self, texto: str) -> str:
        """Remove pontuação.

        :param texto: texto
        :type texto: str
        :return: texto sem pontuação
        :rtype: str
        """

        text = re.sub(self.string_pont, ' ', texto)

        return text

    def remove_stopwords(self, text: str, custom_stopwords: str = None) -> str:
        """Remove as stopwords do texto.

        :param text: texto
        :type text: str
        :param custom_stopwords: stopwords customizadas, defaults to None
        :type custom_stopwords: str, optional
        :return: str
        :rtype: texto sem stopwords
        """

        if custom_stopwords:
            stopwords = custom_stopwords
        else:
            stopwords = self.remove_stop

        text_tokenized = nltk.tokenize.word_tokenize(text)

        for index, word in enumerate(text_tokenized):
            if word in stopwords:
                text_tokenized[index] = ' '
        text = ' '.join(text_tokenized)

        return text

    @staticmethod
    def lower_case(text: str) -> str:
        """Deixa todas as letras em minúsculo.

        :param text: texto
        :type text: str
        :return: texto em minúsculas
        :rtype: str
        """

        text = text.lower()

        return text

    @staticmethod
    def remove_lines(text: str) -> str:
        """Remove linhas duplicadas.

        :param text: texto
        :type text: str
        :return: texto sem linhas duplicadas
        :rtype: str
        """

        text = re.sub(r'\\n', ' ', text)
        text = re.sub(r'\n', ' ', text)

        return text

    @staticmethod
    def remove_spaces(text: str) -> str:
        """Remove espaços duplicados.

        :param text: texto
        :type text: str
        :return: texto sem espaços duplicados.
        :rtype: str
        """

        text = ' '.join(text.split())
        return text

    @staticmethod
    def remove_emoji(text):
        """Remove os emojis no texto.

        :param text: texto
        :type text: str
        :return: texto sem espaços duplicados.
        :rtype: str
        """

        regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                           "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)

    @staticmethod
    def remove_links(text):
        """Remove os links do texto.

        :param text: texto
        :type text: str
        :return: texto sem espaços duplicados.
        :rtype: str
        """
        text = re.sub(r"http\S+", "", text)

        return text

    def fix_text(self, text):
        """Chama os outros métodos na ordem para o tratamento do texto.

        :param text: texto
        :type text: str
        :return: texto sem espaços duplicados.
        :rtype: str
        """

        logger.info(f"Iniciando tratamento do texto número: {self.count}")
        tratador = TrataTexto()
        text = tratador.remove_links(text)
        text = tratador.remove_pont(text)
        text = tratador.remove_accent(text)
        text = tratador.lower_case(text)
        text = tratador.remove_lines(text)
        text = tratador.remove_stopwords(text)
        text = tratador.remove_spaces(text)
        text = tratador.remove_emoji(text)

        self.count += 1
        return text
