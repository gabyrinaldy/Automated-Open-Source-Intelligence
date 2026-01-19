import requests

def get_emails(domain, api_key):
    if not api_key:
        print("[!] API Key do Hunter.io não fornecida. Pulando etapa.")
        return []

    print(f"[*] Buscando emails vazados/públicos para: {domain}...")
    
    # Endpoint da API do Hunter.io
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
    
    found_emails = []
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if 'data' in data and 'emails' in data['data']:
            for email_obj in data['data']['emails']:
                email = email_obj.get('value')
                tipo = email_obj.get('type') # 'personal' ou 'generic'
                found_emails.append(f"{email} ({tipo})")
            
            return found_emails
        elif 'errors' in data:
            print(f"[!] Erro na API Hunter.io: {data['errors'][0]['details']}")
            return []
            
    except Exception as e:
        print(f"[!] Erro ao conectar com Hunter.io: {e}")
        return []