# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [Sadinho Simulator 4.0] - 2025-12-07

### Adicionado
- Simulação de turmas de qualquer tamanho, com página funcional separada para cada aluno.
- Botão "Copy all as table" para copiar os dados de toda a turma em tabela separada por tabulações.
- Níveis alteráveis por tópico, permitindo configurar quantos níveis cada tópico terá.

### Melhorias
- Interface bilíngue (Português / Inglês) para facilitar o uso.

### Alterado
- Botões focados em apenas um aluno (Copy to speedrun, Refresh e Submit) mantidos e adaptados para trabalhar com múltiplos alunos e níveis.
- Layout da barra superior atualizado para inserir número de alunos, tópicos e níveis diretamente na interface, substituindo prompts.

## [3170] - 2025-12-04

### Adicionado
- Adição do **prompt de input para Reaches por tópico**.

---

## [3165] - 2025-04-14

### Alterado
- 5 subtópicos ao invés de 3, visto a mudança no SAD Boletim Infantil.

---

## [3160] - 2024-10-03
### Adicionado
- Atualização no botão **"Copy to speedrun"** para utilizar tabulação (`\t`) como separador, otimizando para exportação.
- Função que remove a última tabulação da string copiada para evitar formatação incorreta.

### Alterado
- Alerta de cópia agora mostra o resultado formatado com tabulações.

## [3155] - 2023-05-31
### Adicionado
- Botão **"Refresh"** para limpar todas as seleções do formulário.
- Botão **"Copy to speedrun"** para copiar os números dos subtópicos selecionados, ignorando os nomes dos tópicos.
  
### Alterado
- Função de cópia para o *clipboard* agora exibe um alerta com o texto copiado.

## [3000] - 2023-04-28
### Adicionado
- Geração dinâmica de tópicos: O número de tópicos é definido pelo usuário através de um *prompt*.
- Cada tópico agora contém três subtópicos gerados dinamicamente.
- Mensagem de fallback adicionada: Tópicos inativos exibem "[inactive]" caso nenhum subtópico seja selecionado.

## [2.0] - 2023-04-28
### Adicionado
- Função de cópia para o *clipboard* ao submeter o formulário.
- Formatação de texto ao copiar, incluindo os tópicos e subtópicos selecionados.

## [1.0] - 2023-04-27
### Adicionado
- Versão inicial com tópicos fixos e três opções de subtópicos.
- Botão de *Submit* sem funcionalidades avançadas.

---

## Documentação Completa das Versões

Aqui está uma linha do tempo completa das versões do projeto com detalhes das funcionalidades

---

### **Versão 1.0**
- **Data de lançamento**: quinta-feira, 27 de abril de 2023, 13:00:21
- **Período ativa**: 11 horas, 13 minutos e 38 segundos
- **Resumo**: Primeira versão básica do formulário com três tópicos e três opções de escolha por tópico.
- **Simulação**: Seleção de tópicos fixos, com três subtópicos por tópico.
- **Funcionalidades**:
  - Formulário com tópicos predefinidos (Topic 1, Topic 2, Topic 3).
  - Três opções de *radio buttons* para cada tópico (Reach 1.1, Reach 1.2, Reach 1.3, etc.).
  - Botão de *Submit* funcional, mas sem grandes ambições ainda.

---

### **Versão 2.0**
- **Data de lançamento**: sexta-feira, 28 de abril de 2023, 00:13:59
- **Período ativa**: 1 hora, 57 minutos e 35 segundos
- **Resumo**: A mágica da cópia para o *clipboard* foi introduzida! 🎩✨
- **Simulação**: Seleção de tópicos fixos e cópia dos resultados no *clipboard* ao submeter o formulário.
- **Funcionalidades**:
  - **Novidade**: Implementação de lógica JavaScript para copiar as opções selecionadas para o *clipboard* ao clicar em "Submit". Sim, o futuro chegou! 🚀
  - Usuário vê um alerta confirmando a cópia após a submissão.
  - Lógica simples: coleta os valores selecionados e os formata para uma string bonitinha (ex: "Topic 1: 1.1"). Beleza pura!

---

### **Versão 3.0 (Build 3000)**
- **Data de lançamento**: sexta-feira, 28 de abril de 2023, 02:11:34
- **Período ativa**: 33 dias, 17 horas, 29 minutos e 43 segundos
- **Resumo**: Agora sim! Perguntando para o usuário quantos tópicos ele quer, porque quem manda aqui é ele. 🎛️
- **Simulação**: Geração automática de N tópicos e subtópicos com base em uma quantidade definida pelo usuário.
- **Funcionalidades**:
  - **Novidade**: O sistema pergunta quantos tópicos gerar, e eles são criados magicamente. Voilà!
  - O sistema gera dinamicamente os tópicos e subtópicos com base na entrada do usuário.
  - Ao submeter o formulário, o sistema copia os tópicos e subtópicos selecionados para o *clipboard* com a formatação adequada (ex: "Topic 1: 1.1").
  - **Melhoria**: Adição de um fallback para tópicos inativos, indicando `[inactive]` se ninguém marcou nada. Simples e prático, né? 😎

---

### **Versão 3155**
- **Data de lançamento**: quarta-feira, 31 de maio de 2023, 19:41:17
- **Período ativa**: 1 ano, 4 meses, 3 dias, 4 horas, 22 minutos e 55 segundos
- **Resumo**: Introdução de dois novos botões mágicos: **"Refresh"** e **"Copy to speedrun"**.
- **Simulação**: Geração dinâmica de tópicos, e agora com direito a reiniciar as escolhas com um clique. 😎
- **Funcionalidades**:
  - **Novidade**: Botão **"Refresh"** para limpar todas as seleções do formulário sem precisar recarregar a página.
  - **Novidade**: Botão **"Copy to speedrun"**, que copia os números dos subtópicos selecionados, ignorando os nomes dos tópicos (ideal para quem não quer perder tempo com detalhes). 🚀
  - O botão de submissão continua funcionando como sempre, mas com um toque a mais: o alerta agora mostra o texto copiado.

---

### **Versão 3160**
- **Data de lançamento**: quinta-feira, 3 de outubro de 2024, 00:04:12
- **Período ativa**: (Versão atual)
- **Resumo**: Agora, as corridas malucas do *speedrun* vão ficar ainda mais eficientes com tabulações em vez de novas linhas! 💨
- **Simulação**: Formato otimizado para facilitar o uso dos resultados copiados em ambientes de simulação, como planilhas. Tabulações = o segredo do sucesso! 😎
- **Funcionalidades**:
  - **Novidade**: Botão "Copy to speedrun" agora copia os números dos subtópicos usando **tabulação** (`\t`) como separador em vez de uma nova linha (`\n`). Rápido como o vento!
  - **Melhoria**: Remoção da última tabulação extra no final da string copiada, porque a perfeição está nos detalhes! ✨
  - Alerta modificado para mostrar os resultados formatados com tabulações, facilitando a vida nas planilhas.

---

### **Versão 3165**
- **Data de lançamento**: terça-feira, 14 de abril de 2025, 16:24
- **Período ativa**: 7 meses, 20 dias, 6 horas e 1 minuto
- **Resumo**: Ajuste na quantidade de subtópicos por tópico, alinhando o simulador com as mudanças do **SAD Boletim Infantil**.
- **Simulação**: Geração dinâmica de tópicos com **5 subtópicos** em vez de 3, permitindo maior fidelidade às estruturas do SAD.
- **Funcionalidades**:
  - **Alterado**: Cada tópico agora contém 5 subtópicos, em vez de 3.
  - Botões **"Refresh"** e **"Copy to speedrun"** continuam funcionando como nas versões anteriores.
  - **Formatação de cópia**: tabulação usada para separar os subtópicos selecionados.
  - **Fallback para tópicos inativos**: se nenhum subtópico for selecionado, o sistema marca `[inactive]`.

---

### **Versão 3170**
- **Data de lançamento**: quinta-feira, 4 de dezembro de 2025, 22:27
- **Período ativa**: Atual
- **Resumo**: Adição do **prompt para definir o número de reaches (subtópicos) por tópico**, permitindo que cada simulação tenha uma quantidade customizável de níveis por tópico.
- **Simulação**: O usuário agora define **quantos tópicos** e **quantos reaches (níveis) por tópico** deseja gerar, tornando o simulador ainda mais flexível e próximo da realidade do SAD.
- **Funcionalidades**:
  - **Adicionado**: Prompt de input para definir a quantidade de reaches por tópico.
  - Funcionalidades de versões anteriores mantidas:
    - **Botão "Refresh"** para limpar todas as seleções.
    - **Botão "Copy to speedrun"** para copiar os níveis selecionados, separados por tabulação.
    - **Formatação de cópia**: tabulação usada para separar os subtópicos selecionados.
    - **Fallback para tópicos inativos**: se nenhum subtópico for selecionado, o sistema marca `[inactive]`.

---

### **Versão 4.0 (Sadinho Simulator 4.0) (Atual)**
- **Data de lançamento**: domingo, 7 de dezembro de 2025, 15:36
- **Período ativa**: Atual
- **Resumo**: Transformação completa do simulador em uma ferramenta para turmas.
- **Simulação**: Turmas de qualquer tamanho, cada aluno com página funcional própria, níveis alteráveis, exportação de dados da turma.
- **Funcionalidades**:
  - **Novidade**: Simulação de turmas de qualquer tamanho, com página funcional para cada aluno.
  - **Novidade**: Botão "Copy all as table" para exportar dados de toda a turma.
  - **Novidade**: Níveis alteráveis por tópico.
  - **Melhoria:** interface bilíngue.
  - **LEGADO**Botões para páginas individuais (Copy to speedrun, Refresh, Submit) mantidos.
    - **Botão "Refresh"** para limpar todas as seleções do aluno.
    - **Botão "Copy to speedrun"** para copiar os níveis na página do aluno, separados por tabulação.
    - **Formatação de cópia**: tabulação usada para separar os subtópicos selecionados.


---

### Resumo dos tempos de "reinado":
1. **Versão 1.0**: 11 horas, 13 minutos e 38 segundos
2. **Versão 2.0**: 1 hora, 57 minutos e 35 segundos
3. **Versão 3000**: 33 dias, 17 horas, 29 minutos e 43 segundos
4. **Versão 3155**: 1 ano, 4 meses, 3 dias, 4 horas, 22 minutos e 55 segundos
5. **Versão 3160**: 6m 11d 16h 20min  
6. **Versão 3165**: 7m 20d 6h 1min  
7. **Versão 3170**: 2 dias, 17 horas e 9 minutos
8. **Versão 4.0**: Atual
