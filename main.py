from fetch import fetch
from parse import parse
from format import format_brief
from send import send_email
from summarize import summarize
URL = "https://www.ruanyifeng.com/blog/atom.xml"

if __name__ == "__main__":
    articles = parse(fetch(URL))
    body = format_brief(articles)+"\n以下是文章摘要\n"+summarize(articles)
    send_email("阮一峰晨报",body)
    
