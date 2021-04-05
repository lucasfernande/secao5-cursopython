import random

inteiro = random.randint(0, 10) # numero inteiro aleatorio
print(inteiro)

flutuante = round(random.uniform(10, 20), 2) # numero decimal aleatorio
# flutuante = random.random() # numero decimal entre 0 e 1
print(flutuante)

lista = ['Luiz', 'Maria', 'Bob', 'Jame', 'Apex']
sorteio = random.choices(lista, k=2) # retorna dois items da lista (pode retornar dois iguais)
sorteio2 = random.sample(lista, k=2) # retorna dois items da lista sem repetir

print(sorteio, sorteio2)

random.shuffle(lista) # embaralha a lista
print(lista)