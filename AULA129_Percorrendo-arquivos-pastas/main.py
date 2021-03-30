import os

caminho_procurado = input('Digite um caminho: ')
termo_procura = input('Digite o termo de procura: ')
contador = 0

def formatar_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'

for root, dirs, files in os.walk(caminho_procurado):
    for file in files:
        if termo_procura in file:
            try:
                contador += 1
                caminho_completo = os.path.join(root, file) # retorna o caminho completo dos arquivos
                nome_arquivo, extensao_arquivo = os.path.splitext(file) # retorna o nome e a extensão do arquivo
                tamanho = os.path.getsize(caminho_completo) # retorna o tamanho do arquivo

                print()
                print(f'Arquivo encontrado: {file}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {extensao_arquivo}')
                print(f'Tamanho: {formatar_tamanho(tamanho)}')
            except PermissionError:
                print('Sem permissão para este arquivo')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except Exception as e:
                print(f'Erro inesperado: {e}')

print()
print(f'Arquivo(s) encontrados: {contador}')