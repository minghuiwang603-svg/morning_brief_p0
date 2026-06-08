import requests 
import feedparser
def fetch(url: str) -> str: 
    resp = requests.get(url)
    return resp.text


def parse(text: str) -> list:
    articles = []
    d = feedparser.parse(text)
    for entry in d.entries:
        articles.append({"title" :entry.title,"link":entry.link})
    return articles


def format_brief(articles: list) -> str:
    result = ""
    for article in articles:
        result += article["title"]
        result += "\n"
        result += article["link"]
        result += "\n\n"
    return result
print(format_brief(parse(fetch("https://www.ruanyifeng.com/blog/atom.xml"))))
