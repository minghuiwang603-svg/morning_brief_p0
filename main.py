from fetch import fetch
from parse import parse
from format import format_brief
URL = "https://www.ruanyifeng.com/blog/atom.xml"
if __name__ == "__main__": 
    print(format_brief(parse(fetch(URL))))