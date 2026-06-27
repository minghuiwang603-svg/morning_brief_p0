from fastapi import FastAPI,HTTPException
from fetch import fetch
from parse import parse
from summarize import summarize
URL = "https://www.ruanyifeng.com/blog/atom.xml"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "晨报服务 Day1 跑通"}
@app.get("/brief")
def brief(count: int = 3):
    try:
        articles = parse(fetch(URL))[:count]
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"晨报源暂时无法访问: {e}")
    summaries = summarize(articles)
    body=[]
    for article, summary in zip(articles, summaries):
        body.append({"title":article["title"] ,"summary":summary,"link":article["link"] })
    return body
