from fpdf import FPDF
import os
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        # Cabeçalho padrão
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'AutoOSINT - Relatório de Reconhecimento', border=0, ln=1, align='C')
        self.line(10, 20, 200, 20)
        self.ln(10)

    def footer(self):
        # Rodapé
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def generate_pdf(domain, whois_data, subdomains, emails, tech_stack):
    # tech_stack agora é esperado como argumento
    
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # --- Título e Data ---
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Alvo: {domain}', ln=1, align='L')
    
    pdf.set_font('Arial', '', 10)
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pdf.cell(0, 10, f'Relatório gerado em: {data_hora}', ln=1, align='L')
    pdf.ln(5)

    # --- Seção 1: WHOIS ---
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '1. Informações de Registro (WHOIS)', ln=1)
    pdf.set_font('Courier', '', 10)
    
    if whois_data:
        try:
            # Tenta extrair campos comuns, mas varia conforme o domínio
            registrar = whois_data.get('registrar', 'N/A')
            creation = whois_data.get('creation_date', 'N/A')
            
            # As vezes creation_date é uma lista, pegamos a primeira data
            if isinstance(creation, list):
                creation = creation[0]
            
            pdf.multi_cell(0, 6, f"Registrar: {registrar}\nCriação: {creation}")
        except:
            pdf.multi_cell(0, 6, "Dados brutos: " + str(whois_data)[:300] + "...")
    else:
        pdf.cell(0, 10, "Dados de WHOIS não disponíveis.", ln=1)
    pdf.ln(5)

    # --- Seção 2: Subdomínios ---
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, f'2. Subdomínios Encontrados ({len(subdomains)})', ln=1)
    pdf.set_font('Arial', '', 11)
    
    if subdomains:
        for sub in subdomains:
            pdf.cell(0, 6, f"- {sub}", ln=1)
    else:
        pdf.cell(0, 6, "Nenhum subdomínio encontrado.", ln=1)
    pdf.ln(5)

    # --- Seção 3: Emails ---
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, f'3. Emails Vazados/Corporativos ({len(emails)})', ln=1)
    pdf.set_font('Arial', '', 11)

    if emails:
        for email in emails:
            pdf.cell(0, 6, f"- {email}", ln=1)
    else:
        pdf.cell(0, 6, "Nenhum email encontrado ou API não configurada.", ln=1)
    pdf.ln(5)

    # --- Seção 4: Tecnologias (NOVO) ---
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, '4. Tecnologias Detectadas', ln=1)
    pdf.set_font('Arial', '', 11)

    if tech_stack:
        for category, tecs in tech_stack.items():
            tecs_str = ", ".join(tecs)
            # Título da categoria em negrito
            pdf.set_font('Arial', 'B', 11)
            pdf.cell(0, 6, f"{category.title()}:", ln=1)
            # Lista de tecnologias normal
            pdf.set_font('Arial', '', 11)
            pdf.multi_cell(0, 6, f"  {tecs_str}")
            pdf.ln(2)
    else:
        pdf.cell(0, 6, "Nenhuma tecnologia identificada.", ln=1)
    
    # --- Salvando o Arquivo ---
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    filename = f"reports/Scan_{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    try:
        pdf.output(filename)
        return filename
    except Exception as e:
        print(f"[!] Erro ao salvar PDF: {e}")
        return None