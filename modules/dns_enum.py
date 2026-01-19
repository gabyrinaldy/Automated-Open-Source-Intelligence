import requests

def get_subdomains(domain):
    subdomains = set()
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.ok:
            data = response.json()
            for item in data:
                subdomains.add(item['name_value'])
    except:
        pass
    return list(subdomains)