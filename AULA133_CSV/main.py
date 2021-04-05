import csv

with open('clientes.csv', 'r') as file:
    # dados = csv.DictReader(file)  # retornando o csv como um dicionario
    dados = [x for x in csv.DictReader(file)]
    # for dado in dados:
    #     print(dado)

with open('clientes2.csv', 'w') as file:
    escreve = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL  # coloca todos os valores entre aspas duplas (definido no quotechar)
    )

    for dado in dados:
        escreve.writerow( # copiando dados do clientes.csv para clientes2.csv
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
