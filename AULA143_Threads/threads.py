from time import sleep
from threading import Thread, Lock

"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


# as threads serão executadas independentes da thread principal
t1 = MeuThread('Thread 1', 6)
t1.start()

t2 = MeuThread('Thread 2', 4)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

#  THREAD PRINCIPAL
for i in range(20):
    print(i)
    sleep(1)

"""

# outra maneira

"""
def demora(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=demora, args=('Thread 1', 5))
t1.start()

t2 = Thread(target=demora, args=('Thread 2', 3))
t2.start()

t3 = Thread(target=demora, args=('Thread 3', 2))
t3.start()

for i in range(10):
    print(i)
    sleep(1)
"""

"""
def demora(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=demora, args=('Thread 1', 5))
t1.start()

while t1.is_alive():
    print('Aguardando a thread ser executada')
    sleep(1)

print('Thread acabou')
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, qtd):
        self.lock.acquire()
        if qtd > self.estoque:
            print('Não temos ingressos suficientes')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= qtd
        print(f'Você comprou {qtd} ingresso(s). Ainda tem {self.estoque} ingresso(s) disponíveis')

        self.lock.release()


if __name__ == '__main__':
    ing = Ingressos(10)

    ts = []
    for i in range(1, 15):
        t = Thread(target=ing.comprar, args=(i,))
        ts.append(t)

    for t in ts:
        t.start()

    executando = True
    while executando:
        executando = False

        for t in ts:
            if t.is_alive():
                executando = True

    print(ing.estoque)
