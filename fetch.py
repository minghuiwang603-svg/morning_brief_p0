import requests 
resp = requests.get("https://example.com")
print(resp.status_code)
print(len(resp.text))