# Analisador de Duplicidades em PDFs

Este projeto é uma ferramenta simples para identificar duplicidades em PDFs, com foco na análise de informações de clientes e vencimentos. Ele utiliza a biblioteca **PyPDF2** para leitura de PDFs, **expressões regulares** para extração de dados e **Tkinter** para a interface gráfica do usuário.


📋 **Funcionalidades**
- Carregamento de arquivos PDF para análise.
- Identificação de clientes e vencimentos duplicados.
- Interface gráfica intuitiva e interativa.
- Exibição dos resultados com destaque para duplicidades.

---

## 🚀 **Como Usar**

### **Pré-requisitos**
- **Python 3.6+** instalado em seu sistema.
- Bibliotecas necessárias:
  -  PyPDF2`
  - `tkinter`

Instale as dependências executando:
```bash
pip install PyPDF2
Execução
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Execute o script Python:

bash
Copiar código
python nome_do_arquivo.py
Na interface gráfica:

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


🤝 Contribuições
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

Faça um fork do repositório.
Crie uma branch para a sua funcionalidade:
bash
Copiar código
git checkout -b minha-nova-funcionalidade
Faça as alterações desejadas e commit:
bash
Copiar código
git commit -m "Adicionei uma nova funcionalidade"
Envie as alterações para o seu fork:
bash
Copiar código
git push origin minha-nova-funcionalidade
Abra um Pull Request para revisão.
📝 Licença
Este projeto está licenciado sob a MIT License.

📧 Contato
Desenvolvido por: [Seu Nome]
Email: [seu-email@example.com]
GitHub: https://github.com/seu-usuario
yaml
Copiar código

---

### **Passos para Colocar no GitHub**
1. Salve este conteúdo em um arquivo chamado `README.md`.
2. Coloque o arquivo na raiz do seu repositório.
3. Faça o commit e envie para o GitHub:
   ```bash
   git add README.md
   git commit -m "Adicionado arquivo README.md"
   git push origin main
Agora, o GitHub exibirá este README.md automaticamente na página inicial do seu repositório. Se precisar de mais ajuda, é só avisar! 😊
