from string import Template
from datetime import datetime

data_atual = datetime.now().strftime('%d/%m/%Y')

with open('template.html', 'r', encoding='utf-8') as html:
    template = Template(html.read())
    body = template.substitute(nome='Lucas', data=data_atual)

print(body)
