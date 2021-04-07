import requests
from bs4 import BeautifulSoup

# o requests faz a requisição
# o bs4 permite a manipulação do html dos sites dentro do script

url = 'https://pt.stackoverflow.com/questions/tagged/python'

response = requests.get(url)  # obtendo os dados da url
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink').text  # pegando o título das perguntas
    data = pergunta.select_one('.relativetime').text  # pegando a data das perguntas
    votos = pergunta.select_one('.vote-count-post ').text  # pegando os votos das perguntas

    print(data, titulo, votos, sep='\t')
