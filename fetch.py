import requests 
import feedparser
resp = requests.get("https://www.ruanyifeng.com/blog/atom.xml")
d = feedparser.parse(resp.text)
articles = []
print(f"状态码: {resp.status_code}")
print(f"Content-Type: {resp.headers['Content-Type']}")
print(f"Server: {resp.headers['Server']}")
print(f"Date: {resp.headers['Date']}")
for entry in d.entries:
    articles.append({"title" :entry.title,"link":entry.link})
print(articles)