import requests 
resp = requests.get("https://www.ruanyifeng.com/blog/atom.xml")
print(f"状态码: {resp.status_code}")
print(f"Content-Type: {resp.headers['Content-Type']}")
print(f"Server: {resp.headers['Server']}")
print(f"Date: {resp.headers['Date']}")
print(resp.text[:300])