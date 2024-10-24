import fitz  # PyMuPDF
import os
import csv
import re  # Para expressões regulares
import tkinter as tk
from tkinter import filedialog

# Função para selecionar o arquivo PDF
def selecionar_pdf():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo PDF",
        filetypes=[("PDF files", "*.pdf")])
    return file_path

# Função para selecionar a pasta de destino
def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    folder_path = filedialog.askdirectory(title="Selecione a pasta para salvar os boletins")
    return folder_path

# Função para extrair RA, nome do aluno e turma da página
def extrair_dados_pagina(pagina):
    texto = pagina.get_text("text")
    linhas = texto.split("\n")
    ra = None
    nome_info = None
    turma = None
    
    # Expressão regular para capturar o código da turma (5 caracteres)
    regex_turma = r"\b[A-Z]{2}\d[A-Z]{2}\b"
    
    for linha in linhas:
        if "Educação Infantil" in linha or "EFAI" in linha:  # Ajuste conforme necessário
            partes = linha.split(" - ")
            if len(partes) > 1:
                ra = partes[0].strip()
                nome_info = partes[1].split("Educação Infantil")[0].strip()
                
                # Tentando capturar o código da turma
                match_turma = re.search(regex_turma, linha)
                if match_turma:
                    turma = match_turma.group(0)
                break
    return ra, nome_info, turma

# Função principal para processar o PDF
def processar_pdf(pdf_path, output_folder):
    # Abrindo o PDF
    pdf_document = fitz.open(pdf_path)
    total_pages = pdf_document.page_count

    # Inicializando variáveis para logs por turma
    logs_por_turma = {}

    # Percorrendo todas as páginas do PDF
    pagina_atual = 0
    while pagina_atual < total_pages:
        pagina = pdf_document.load_page(pagina_atual)
        ra, nome_aluno, turma = extrair_dados_pagina(pagina)

        if ra and nome_aluno and turma:
            # Procurando o intervalo de páginas do boletim
            inicio_boletim = pagina_atual
            while pagina_atual < total_pages:
                proxima_pagina = pdf_document.load_page(pagina_atual)
                ra_prox, _, _ = extrair_dados_pagina(proxima_pagina)
                if ra_prox != ra:
                    break
                pagina_atual += 1

            fim_boletim = pagina_atual - 1

            # Criando o nome do arquivo e a pasta da turma
            pasta_turma = os.path.join(output_folder, turma)
            os.makedirs(pasta_turma, exist_ok=True)

            nome_arquivo = f"{ra}.pdf"
            caminho_arquivo = os.path.join(pasta_turma, nome_arquivo)

            # Extraindo as páginas e salvando o boletim em um arquivo PDF separado
            boletim_pdf = fitz.open()
            for i in range(inicio_boletim, fim_boletim + 1):
                boletim_pdf.insert_pdf(pdf_document, from_page=i, to_page=i)
            boletim_pdf.save(caminho_arquivo)
            boletim_pdf.close()

            # Adicionando informações ao log
            if turma not in logs_por_turma:
                logs_por_turma[turma] = {'alunos': [], 'paginas': []}

            logs_por_turma[turma]['alunos'].append([ra, nome_aluno])
            logs_por_turma[turma]['paginas'].append([ra, nome_aluno, inicio_boletim + 1, fim_boletim + 1, fim_boletim - inicio_boletim + 1, nome_arquivo])

    # Salvando os logs por turma
    for turma, logs in logs_por_turma.items():
        pasta_turma = os.path.join(output_folder, turma)
        # Salvando os logs em formato CSV dentro da pasta da turma
        with open(os.path.join(pasta_turma, 'log_alunos.csv'), mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['RA', 'Nome'])
            writer.writerows(logs['alunos'])

        with open(os.path.join(pasta_turma, 'log_paginas.csv'), mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['RA', 'Nome', 'Página Inicial', 'Página Final', 'Total de Páginas', 'Arquivo'])
            writer.writerows(logs['paginas'])

    # Fechando o PDF principal
    pdf_document.close()

# Iniciando o processo com seleção de PDF e pasta
pdf_path = selecionar_pdf()
if pdf_path:
    output_folder = selecionar_pasta()
    if output_folder:
        processar_pdf(pdf_path, output_folder)
        print(f"Processamento concluído! Boletins salvos em: {output_folder}")
    else:
        print("Nenhuma pasta de destino foi selecionada.")
else:
    print("Nenhum arquivo PDF foi selecionado.")
