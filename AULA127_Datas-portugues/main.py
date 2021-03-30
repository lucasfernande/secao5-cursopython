from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

data = datetime.now()
formato = data.strftime('%A, %d de %B de %Y')
print(formato)         # dia da semana, dia de mês de ano

formato2 = data.strftime('%d/%m/%Y %H:%M:%S')
print(formato2)


mes = int(data.strftime('%m')) # pegando o mês atual
print(f'Mês atual: {mes}, dias: {mdays[mes]}') # quantos dias tem o mês atual