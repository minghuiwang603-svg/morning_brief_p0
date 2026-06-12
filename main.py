from fetch import fetch
from parse import parse
from format import format_brief
from send import send_email
URL = "https://www.ruanyifeng.com/blog/atom.xml"
if __name__ == "__main__":
    send_email("阮一峰晨报",format_brief(parse(fetch(URL))))
    
