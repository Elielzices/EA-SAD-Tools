# Sadinho Splitter

Este script automatiza o processo de extração de boletins de alunos a partir de um arquivo PDF contendo múltiplos boletins. Cada boletim é separado e salvo como um arquivo PDF individual, organizado por turma. Logs com informações dos alunos e a estrutura de páginas são gerados automaticamente em formato CSV.

## Download

Para usar a versão mais recente, faça o download direto:

[Splitter Sadinho Results 1.0 (EXE)](https://github.com/Elielzices/EA-SAD-Tools/releases/download/SplitterSadinho/SplitterSadinhoResults-1.0.exe)
[Splitter Sadinho Results 1.0 (PYTHON)](https://github.com/Elielzices/EA-SAD-Tools/releases/download/SplitterSadinho/SplitterSadinhoResults-1.0.py)

## Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `PyMuPDF (fitz)`
  - `csv`
  - `os`
  - `re`
  - `tkinter` (para interface de seleção de arquivos e diretórios)

### Instalação das bibliotecas:

```bash
pip install PyMuPDF
```

**Nota:** O `tkinter` já vem com a maioria das instalações do Python. Se você estiver em Linux e precisar instalá-lo, utilize:

```bash
sudo apt-get install python3-tk
```

## Modo de Uso

1. **Clonar o repositório**:
   Clone o repositório para sua máquina local.

2. **Rodar o script**:
   Execute o script Python para iniciar o processo de extração e organização dos boletins.

```bash
SplitterSadinhoResults-1.0.py
```

3. **Passos Interativos**:
   - Selecione o **arquivo PDF** com os boletins.
   - Escolha a **pasta de destino** onde os arquivos separados serão salvos.
   - O script irá processar o PDF, salvar os boletins em arquivos PDF separados e organizar os arquivos por turma.
   - Na pasta de cada turma, você encontrará dois logs em formato CSV: 
     - `log_alunos.csv` contendo o RA e o nome dos alunos.
     - `log_paginas.csv` com o intervalo de páginas e a quantidade de páginas por aluno.

## Estrutura do Código

### Funções Principais

#### `selecionar_pdf()`
Essa função utiliza o `tkinter.filedialog` para abrir uma janela de seleção de arquivo, permitindo ao usuário escolher o arquivo PDF de boletins.

#### `selecionar_pasta()`
Função semelhante à anterior, mas utilizada para selecionar a pasta de destino onde os boletins e logs serão salvos.

#### `extrair_dados_pagina(pagina)`
Extrai os principais dados de cada página do boletim, como o **RA** (Registro Acadêmico), **nome do aluno** e **código da turma**. A turma é identificada através de uma expressão regular que captura um padrão de 5 caracteres (como "EI3MA", "EF1TB", etc.).

#### `processar_pdf(pdf_path, output_folder)`
Essa é a função principal que:
- Abre o PDF com `PyMuPDF (fitz)`.
- Percorre cada página, extrai os dados do aluno e determina o intervalo de páginas de cada boletim.
- Salva os boletins em PDFs separados, organizando-os por turma.
- Gera arquivos CSV de log para cada turma, com as informações do RA, nome do aluno, intervalo de páginas e quantidade de páginas por boletim.

### Módulo `fitz` (PyMuPDF)

#### Principais Funções Usadas:
- **`fitz.open(pdf_path)`**: Abre o arquivo PDF para processamento.
- **`pdf_document.load_page(pagina_atual)`**: Carrega uma página específica do PDF para extrair seu conteúdo.
- **`pagina.get_text("text")`**: Extrai o texto de uma página, que é usado para identificar o RA, nome e turma.
- **`boletim_pdf.insert_pdf(...)`**: Insere uma ou mais páginas de outro PDF no PDF em criação.
- **`boletim_pdf.save(caminho_arquivo)`**: Salva o PDF resultante no caminho especificado.

### Exemplo de Execução

Ao rodar o script, ele solicita a seleção do PDF e da pasta de destino. Depois, o processamento organiza os boletins na seguinte estrutura:

```
/output
  ├── EI3MA
  │   ├── 1234.pdf
  │   ├── 2345.pdf
  │   ├── log_alunos.csv
  │   └── log_paginas.csv
  ├── EF1TB
  │   ├── 3456.pdf
  │   ├── 4567.pdf
  │   ├── log_alunos.csv
  │   └── log_paginas.csv
```

## Logs

- **`log_alunos.csv`**: Lista o **RA** e o **Nome** de cada aluno.
- **`log_paginas.csv`**: Detalha o **intervalo de páginas** (inicial e final), o **número de páginas** e o **nome do arquivo PDF** gerado para cada aluno.

## Contribuições

- Aceitamos contribuições para melhorias no código e na documentação. Sinta-se à vontade para abrir issues ou pull requests no repositório!

## Licença

Este projeto é distribuído sob a licença MIT.
