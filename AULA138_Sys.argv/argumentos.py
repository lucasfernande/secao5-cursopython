# EXECUTAR NO TERMINAL

import sys
import os

args = sys.argv
qtd_args = len(args)

if qtd_args <= 1:
    print('Erro: faltando argumentos')
    print('-a', 'Lista todos os arquivos nessa pasta', sep='\t')
    print('-d', 'Lista todos os diretórios nessa pasta', sep='\t')
    sys.exit()

apenas_arquivos = False
if '-a' in args:
    apenas_arquivos = True

apenas_diretorios = False
if '-d' in args:
    apenas_diretorios = True

for arquivo in os.listdir('.'):  # caso digitar -a, será exibido apenas arquivos. Caso digitar -d, será exibido pastas
    if apenas_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if apenas_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)
