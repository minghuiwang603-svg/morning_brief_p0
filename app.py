from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fetch import fetch
from parse import parse
from summarize import summarize
from pydantic import BaseModel
URL = "https://www.ruanyifeng.com/blog/atom.xml"

app = FastAPI()

class Article(BaseModel):
    title: str
    link: str
    summary: str  

@app.get("/")
def home():
    return {"message": "晨报服务 Day1 跑通"}
@app.get("/brief", response_model=list[Article])
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

@app.get("/web", response_class=HTMLResponse)
def web():
    articles_data = brief(count=3)
    html_str = "<html><body><h1>今日晨报</h1>" 
    for item in articles_data:
        title = item["title"]                                            
        link = item["link"]                                              
        summary = item["summary"] 
        html_str += f"<h2><a href='{link}'>{title}</a></h2>" 
        html_str += f"<p>{summary}</p>"
        html_str += "<hr>" 
    html_str += "</body></html>"
    return HTMLResponse(content=html_str)