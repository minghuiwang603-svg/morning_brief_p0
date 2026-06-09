import feedparser
def parse(text: str) -> list:
    articles = []
    d = feedparser.parse(text)
    for entry in d.entries:
        articles.append({"title" :entry.title,"link":entry.link})
    return articles

