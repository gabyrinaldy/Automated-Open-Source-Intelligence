import builtwith

def get_tech(domain):
    print(f"[*] Identificando tecnologias do site: {domain}...")
    
    # Adiciona protocolo se não tiver, pois o builtwith precisa de URL completa
    if not domain.startswith("http"):
        url = f"http://{domain}"
    else:
        url = domain

    try:
        # O builtwith retorna um dicionário: {'cms': ['WordPress'], 'server': ['Nginx']}
        technologies = builtwith.parse(url)
        return technologies
    except Exception as e:
        print(f"[!] Erro ao detectar tecnologias: {e}")
        return {}