import openpyxl

pedidos = openpyxl.load_workbook('pedidos.xlsx')
planilhas = pedidos.sheetnames  # pegando o nome das páginas

planilha1 = pedidos['Página1']
print(planilha1['b4'].value)  # acessando o conteudo do campo da coluna B linha 4

print('#' * 40)
for campo in planilha1['b']: # acessando toda a coluna B
    if campo.value is not None:
        print(campo.value)

print('#' * 40)

for linha in planilha1['a1:c2']: # acessando o conteudo em determinado intervalo (a1:c2)
    for coluna in linha:
        print(coluna.value)
