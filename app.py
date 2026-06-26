from fastapi import FastAPI
from fetch import fetch
from parse import parse
from summarize import summarize
URL = "https://www.ruanyifeng.com/blog/atom.xml"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "晨报服务 Day1 跑通"}

@app.get("/brief")
def brief():
    articles = parse(fetch(URL))
    summaries = summarize(articles)
    body=[]
    for article, summary in zip(articles, summaries):
        body.append({"title":article["title"] ,"summary":summary,"link":article["link"] })
    return body
    