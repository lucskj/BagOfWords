import requests
from bs4 import BeautifulSoup
import spacy


# Função responsável por filtrar e remover partes específicas da página.
def removerTags(soup):
    for data in soup(['style', 'script', 'head', 'header', 'meta', '[document]', 'title', 'footer', 'iframe', 'nav']):
        data.decompose()
        
    # Retornando todas as expressões em uma string, separando por espaço.
    return ' '.join(soup.stripped_strings)   


# Carregando a biblioteca Spacy, baseando-se na língua inglesa.
nlp = spacy.load("en_core_web_sm")

# Variáveis para armazenar o link de cada página.
urls = ['https://hbr.org/2022/04/the-power-of-natural-language-processing',
        'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html',
        'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP',
        'https://monkeylearn.com/natural-language-processing/',
        'https://en.wikipedia.org/wiki/Natural_language_processing']

# Definindo arrays para armazenar o resultado de todos os textos.
textoCompleto = []

# Loop para passar por cada url.
for url in urls:
  html = requests.get(url).text                     # Armazenando o conteúdo de toda a página.
  soup = BeautifulSoup(html, 'html.parser')         # Removendo parte da estrutura HTML do texto.
  texts = removerTags(soup)                         # Enviando o texto para filtrar.
  page = nlp(texts)

  # Armazenando as sentenças na lista geral.
  for sentence in page.sents:
    textoCompleto.append(sentence.text)

# Printando o resultado da lista, para checagem.
print(textoCompleto)

# Definição de uma variável para armazenar o vocabulário.
vocabulario = set()
for sentence in textoCompleto:
  for palavra in sentence.split():
    vocabulario.add(palavra)

vocabulario = sorted(vocabulario)
bagOfWords = []

for sentence in textoCompleto:
  vetor = [0] * len(vocabulario)
  for palavra in sentence.split():
    vetor[vocabulario.index(palavra)] += 1
  
  print(vetor)
  bagOfWords.append(vetor)