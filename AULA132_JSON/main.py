import json
from dados import *

clientesJSON = json.dumps(clientes_dicionario, indent=4)  # convertendo um dicionario para JSON
print(clientesJSON)

clientesDIC = json.loads(clientes_json)  # convertendo um JSON para dicionario
# for key, value in clientesDIC.items():
#     print(key, value)

with open('clientes.json', 'w') as file:
    json.dump(clientes_dicionario, file, indent=4)  # salvando o dicionario em um arquivo JSON

with open('clientes.json', 'r') as file:
    dados = json.load(file) # lendo o arquivo JSON

for key, value in dados.items():
    print(key, value)
