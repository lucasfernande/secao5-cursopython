"""

Pilhas e filas

Pilha (stack) - LIFO - last in e first out
    Exemplo: pilha de livros - o último a entrar é o primeiro a sair

Fila (queue) - FIFO - first in e first out
    Exemplo: fila de banco - o primeiro a entrar é o primeiro a sair

Filas podem afetar o desempenho, porque a cada item alterado, todos os índices serão
modificados.

"""

# LIFO

"""

livros = ['Livro 1', 'Livro 2', 'Livro 3', 'Livro 4', 'Livro 5']  # o livro 5 foi o último a entrar
livro_removido = livros.pop()
print(livros, livro_removido)

"""

# FIFO

from collections import deque
from time import sleep

"""

fila = deque()
fila.append('Joãozinho')  # joãozinho foi o primeiro a entrar
fila.append('Maria')
fila.append('Mariana')
fila.append('Luiz')
print(fila)

print(f'Saiu: {fila.popleft()}')  # joãozinho vai ser o primeiro a sair
print(f'Saiu: {fila.popleft()}')
print(fila)

"""

nums = deque(maxlen=10)  # maxlen = define o máximo de itens que a lista pode ter

for i in range(100):
    nums.append(i)  # quando a lista tiver 10 itens, o primeiro item será removido
    sleep(1)
    print(nums)
