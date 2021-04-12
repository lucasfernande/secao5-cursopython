import PyPDF2
import os

caminhos_pdfs = 'pdf'

# Unindo os pdfs

"""
novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminhos_pdfs):
    for file in files:
        caminho_completo = os.path.join(root, file)

        pdf = open(caminho_completo, 'rb')
        novo_pdf.append(pdf)  # juntando o contéudo do arquivo1.pdf e o arquivo2.pdf em um só

with open(f'{caminhos_pdfs}/novo_pdf.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)  # escrevendo o conteúdo dos arquivos em um novo arquivo
"""

# Separando os pdfs por página

with open('pdf/novo_pdf.pdf', 'rb') as arquivo_pdf:
    reader = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = reader.getNumPages() # pegando o numero de paginas do pdf

    for pagina in range(num_paginas):
        writer = PyPDF2.PdfFileWriter()
        pagina_atual = reader.getPage(pagina)

        writer.addPage(pagina_atual)

        with open(f'novos_pdfs/pagina{pagina}.pdf', 'wb') as novo_pdf:
            writer.write(novo_pdf)

