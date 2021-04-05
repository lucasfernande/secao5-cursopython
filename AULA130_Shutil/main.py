import os
import shutil

caminho_original = r'C:\Users\lucas\Documents\teste'
caminho_novo =  r'C:\Users\lucas\Documents\teste2'

try:
    os.mkdir(caminho_novo) # criando uma nova pasta
except FileExistsError:
    print(f'Essa pasta ({caminho_novo}) já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        shutil.move(old_file_path, new_file_path) # movendo os arquivos da pasta teste para a teste2
        print(f'Arquivo {file} movido!')

        shutil.copy(new_file_path, old_file_path) # copiando os arquivos de volta para a pasta teste
        print(f'Arquivo {file} copiado!')