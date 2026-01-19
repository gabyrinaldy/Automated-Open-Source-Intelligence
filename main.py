import sys
import time
# Importando todos os módulos, incluindo o novo tech_detect
from modules import whois_info, dns_enum, email_harvest, report_generator, tech_detect

# Códigos de cores para o terminal
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_banner():
    print(GREEN)
    print(r"""
       _         _        ___  ____ ___ _   _ _____ 
      / \  _   _| |_ ___ / _ \/ ___|_ _| \ | |_   _|
     / _ \| | | | __/ _ \ | | \___ \| ||  \| | | |  
    / ___ \ |_| | || (_) | |_| |___) | || |\  | | |  
   /_/   \_\__,_|\__\___/ \___/|____/___|_| \_| |_|  
    """)
    print(f"""    AutoOSINT - Ferramenta de Reconhecimento Automatizado
    -----------------------------------------------------
    {RESET}""")

def main():
    print_banner()
    
    # --- Coleta de Inputs ---
    try:
        domain = input(f"[*] Digite o domínio alvo (ex: site.com): {RESET}").strip()
        if not domain:
            print(f"{RED}[!] Domínio inválido.{RESET}")
            sys.exit()
            
        hunter_api = input(f"[*] (Opcional) Digite sua API Key do Hunter.io: {RESET}").strip()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Execução interrompida pelo usuário.{RESET}")
        sys.exit()

    print(f"\n{YELLOW}[+] Iniciando reconhecimento contra: {domain}...{RESET}")
    start_time = time.time()

    # --- FASE 1: WHOIS ---
    print(f"\n{GREEN}[+] [1/5] Coletando informações WHOIS...{RESET}")
    whois_data = whois_info.get_whois(domain)
    if whois_data:
        registrante = whois_data.get('registrar') or whois_data.get('org') or 'Desconhecido'
        print(f"    -> Registrante: {registrante}")
    else:
        print(f"{RED}    -> Falha ao obter WHOIS.{RESET}")

    # --- FASE 2: Subdomínios ---
    print(f"\n{GREEN}[+] [2/5] Mapeando subdomínios (crt.sh)...{RESET}")
    subdomains = dns_enum.get_subdomains(domain)
    print(f"    -> Encontrados: {len(subdomains)} subdomínios únicos")
    
    if subdomains:
        for s in subdomains[:5]: # Mostra só os 5 primeiros
            print(f"       - {s}")
        if len(subdomains) > 5:
            print(f"       ... e mais {len(subdomains)-5}")

    # --- FASE 3: Email Harvesting ---
    print(f"\n{GREEN}[+] [3/5] Buscando e-mails vazados/corporativos...{RESET}")
    emails = []
    if hunter_api:
        emails = email_harvest.get_emails(domain, hunter_api)
        print(f"    -> Encontrados: {len(emails)} e-mails")
    else:
        print(f"{YELLOW}    -> Pulo: API Key não fornecida.{RESET}")

    # --- FASE 4: Tech Detection (NOVO) ---
    print(f"\n{GREEN}[+] [4/5] Detectando tecnologias (Stack)...{RESET}")
    tech_stack = tech_detect.get_tech(domain)
    
    if tech_stack:
        for category, tec in tech_stack.items():
            print(f"    -> {category}: {', '.join(tec)}")
    else:
        print(f"{YELLOW}    -> Nenhuma tecnologia identificada.{RESET}")

    # --- FASE 5: Relatório ---
    print(f"\n{GREEN}[+] [5/5] Gerando relatório final...{RESET}")
    
    # Passamos todas as variáveis coletadas
    report_path = report_generator.generate_pdf(domain, whois_data, subdomains, emails, tech_stack)
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)

    # --- CONCLUSÃO ---
    print(f"\n{GREEN}--- SCAN CONCLUÍDO EM {duration} SEGUNDOS ---{RESET}")
    if report_path:
        print(f"📄 Relatório salvo em: {YELLOW}{report_path}{RESET}")
    else:
        print(f"{RED}[!] Erro ao salvar o relatório.{RESET}")

if __name__ == "__main__":
    main()