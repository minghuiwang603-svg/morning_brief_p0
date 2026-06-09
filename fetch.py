import requests 

def fetch(url: str) -> str: 
    resp = requests.get(url)
    return resp.text

