from datetime import datetime, timedelta

data = datetime(2021, 3, 26, 14, 19)
#   ano/mes/dia. hora, minuto e segundo são opcionais
print(data)  # a data é exibida no padrão americano

print(data.strftime('%d/%m/%Y %H:%M'))  # formatando a data para o padrão brasileiro

data2 = datetime.strptime('26/03/2021', '%d/%m/%Y')
print(data2.timestamp())  # conta os segundos desde o unix epoch (1970-01-01 00:00)

data3 = datetime.fromtimestamp(1616727600)  # convertendo o timestamp para segundos
print(data3)

data4 = datetime.strptime('19/06/1994 20:00:00', '%d/%m/%Y %H:%M:%S')
data4 += timedelta(days=5, seconds=48) # somando 5 dias e 48 segundos
print(data4.strftime('%d/%m/%Y %H:%M:%S'))
