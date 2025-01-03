# Analisador de Duplicidades em PDFs

Este projeto é uma ferramenta simples para identificar duplicidades em PDFs, com foco na análise de informações de clientes e vencimentos. Ele utiliza a biblioteca **PyPDF2** para leitura de PDFs, **expressões regulares** para extração de dados e **Tkinter** para a interface gráfica do usuário.

---

## 📋 **Funcionalidades**
- Carregamento de arquivos PDF para análise.
- Identificação de clientes e vencimentos duplicados.
- Interface gráfica intuitiva e interativa.
- Exibição dos resultados com destaque para duplicidades.

---

## 🚀 **Como Usar**

### **Pré-requisitos**
- **Python 3.6+** instalado em seu sistema.
- Bibliotecas necessárias:
  - `PyPDF2`
  - `tkinter`
  - `collections`
  - `re`

Instale as dependências executando:
```bash
pip install PyPDF2
```

Clique no botão Carregar PDF.
Selecione um arquivo PDF para análise.
Visualize os resultados diretamente na janela.
🛠 Configurações
Regex Padrões
Nome do cliente: DADOS DO CLIENTE\s+([A-Z\s]+)
Datas de vencimento: VENCIMENTO\s*(\d{2}/\d{2}/\d{4})
Você pode ajustar os padrões no código para atender a diferentes formatos de PDF.

🎨** Interface Gráfica**
Linguagem: Tkinter
Recursos:
Campo de texto com rolagem para exibição dos resultados.
Estilo customizado com tema escuro.
🖥 Capturas de Tela
Tela Principal:




📧 Contato
Desenvolvido por: [Kauan Pollicarpo]
Email: [Kauanpolicarpo0@gmail.com]
GitHub: https://github.com/seu-usuario

