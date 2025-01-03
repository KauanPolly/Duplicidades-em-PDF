import PyPDF2
import re
from collections import defaultdict

def ler_pdf(arquivo_pdf):
    try:
        with open(arquivo_pdf, 'rb') as pdf_file:
            leitor = PyPDF2.PdfReader(pdf_file)
            texto_completo = ""
            for i, pagina in enumerate(leitor.pages):
                texto_completo += pagina.extract_text()
                print(f"Texto da Página {i + 1}:\n{pagina.extract_text()}\n")
            return texto_completo
    except Exception as e:
        print(f"Erro ao Ler PDF, Motivo: {e}")
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

# Caminho para o arquivo PDF
caminho_pdf = "boletoduplicados2pdf.pdf"
conteudo = ler_pdf(caminho_pdf)

if conteudo:
    print("\nTexto extraído com sucesso!")
    duplicidades = identificar_duplicidades(conteudo)
    if duplicidades:
        print("\n=== DUPLICIDADES ENCONTRADAS ===")
        for cliente, vencimentos in duplicidades.items():
            print(f"Cliente: {cliente}, Datas de Vencimento Duplicadas: {', '.join(vencimentos)}")
    else:
        print("Nenhuma duplicidade encontrada.")
