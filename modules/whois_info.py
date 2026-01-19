import whois

def get_whois(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"Erro no WHOIS: {e}"