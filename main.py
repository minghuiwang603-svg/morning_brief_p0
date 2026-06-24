from fetch import fetch
from parse import parse
from send import send_email
from summarize import summarize
URL = "https://www.ruanyifeng.com/blog/atom.xml"

if __name__ == "__main__":
    articles = parse(fetch(URL))
    summaries = summarize(articles)
    body = ""
    for article, summary in zip(articles, summaries):
        body += article["title"] + "\n" + summary + "\n" + article["link"] + "\n\n"
    send_email("阮一峰晨报", body)
    
