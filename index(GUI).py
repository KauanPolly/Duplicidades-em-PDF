import PyPDF2
import re
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
from tkinter.font import Font

def ler_pdf(arquivo_pdf):
    try:
        with open(arquivo_pdf, 'rb') as pdf_file:
            leitor = PyPDF2.PdfReader(pdf_file)
            texto_completo = ""
            for i, pagina in enumerate(leitor.pages):
                texto_completo += pagina.extract_text()
            return texto_completo
    except Exception as e:
        messagebox.showerror("Erro ao Ler PDF", f"Erro ao Ler PDF, Motivo: {e}")
        return None

def identificar_duplicidades(texto):
    clientes = defaultdict(list)

    # Expressões regulares corrigidas
    padrao_nome = r'DADOS DO CLIENTE\s+([A-Z\s]+)'
    padrao_vencimento = r'VENCIMENTO\s*(\d{2}/\d{2}/\d{4})'

    # Encontrar nomes e vencimentos
    nomes = re.findall(padrao_nome, texto)
    vencimentos = re.findall(padrao_vencimento, texto)

    # Agrupar vencimentos por cliente
    for i, nome in enumerate(nomes):
        vencimento = vencimentos[i] if i < len(vencimentos) else "Desconhecido"
        clientes[nome.strip()].append(vencimento)

    # Verificar duplicidades
    duplicidades = {}
    for cliente, lista_vencimentos in clientes.items():
        duplicados = {data for data in lista_vencimentos if lista_vencimentos.count(data) > 1}
        if duplicados:
            duplicidades[cliente] = list(duplicados)

    return duplicidades

def carregar_pdf():
    caminho_pdf = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if not caminho_pdf:
        return

    conteudo = ler_pdf(caminho_pdf)
    if conteudo:
        duplicidades = identificar_duplicidades(conteudo)
        exibir_resultados(duplicidades)

def exibir_resultados(duplicidades):
    texto_resultado.delete(1.0, tk.END)

    if duplicidades:
        texto_resultado.insert(tk.END, "=== DUPLICIDADES ENCONTRADAS ===\n")
        for cliente, vencimentos in duplicidades.items():
            texto_resultado.insert(tk.END, f"Cliente: ")
            texto_resultado.insert(tk.END, cliente, ("bold"))
            texto_resultado.insert(tk.END, f", Datas de Vencimento Duplicadas: {', '.join(vencimentos)}\n")
    else:
        texto_resultado.insert(tk.END, "Nenhuma duplicidade encontrada.\n")

# Configurar a interface gráfica
janela = tk.Tk()
janela.title("Analisador de Duplicidades em PDFs")
janela.geometry("800x600")
janela.resizable(False, False)
janela.configure(bg="#2b2b2b")

# Estilo
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 14, "bold"), padding=10, background="#5bc0de", foreground="#ffffff")
style.map("TButton", background=[("active", "#357ab7")])

# Fonte personalizada
titulo_fonte = Font(family="Arial", size=18, weight="bold")
resultado_fonte = Font(family="Courier", size=12)

# Configuração de tag para o texto em negrito
texto_resultado = scrolledtext.ScrolledText(wrap=tk.WORD, width=90, height=20, font=resultado_fonte, bg="#1c1c1c", fg="#f0f0f0", insertbackground="white")
texto_resultado.tag_configure("bold", font=("Courier", 12, "bold"))

# Título
lbl_titulo = tk.Label(janela, text="Analisador de Duplicidades em PDFs", font=titulo_fonte, bg="#2b2b2b", fg="#f0f0f0")
lbl_titulo.pack(pady=20)

# Botão para carregar o PDF
btn_carregar = ttk.Button(janela, text="Carregar PDF", command=carregar_pdf)
btn_carregar.pack(pady=20)

# Área de texto para exibir os resultados
texto_frame = tk.Frame(janela, bg="#2b2b2b")
texto_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
texto_resultado.pack(fill=tk.BOTH, expand=True)

# Rodapé
lbl_rodape = tk.Label(janela, text="Desenvolvido por [Seu Nome]", font=("Arial", 10), bg="#2b2b2b", fg="#888888")
lbl_rodape.pack(pady=10)

# Iniciar a interface gráfica
janela.mainloop()
