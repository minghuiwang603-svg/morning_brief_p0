import os
from dotenv import load_dotenv
from openai import OpenAI
import re


def clean_html(text):   
    return re.sub(r"<[^>]+>", "", text)
    

def summarize(articles: list) -> str:
    # —— 第1块：把所有标题拼成一段文本 ——
    # for 遍历 articles，把每个 article["title"] 接进一个字符串，每个后面加 "\n"
    content=""
    for i, article in enumerate(articles, 1):            
        content += "【" + str(i) + "】" + article["title"] + "\n" + clean_html(article["body"]) + "\n\n"
    # —— 第2块：造 client（照抄你 Day17 test_llm.py 那三行：load_dotenv / 取 key / OpenAI(...)）——
    load_dotenv()
    d_key=os.environ.get("DEEPSEEK_API_KEY")
    client = OpenAI(api_key=d_key,base_url="https://api.deepseek.com")
    # —— 第3块：调 DeepSeek，messages 两条 ——
    response=client.chat.completions.create(
        model="deepseek-chat",
        temperature=0,
        messages=[
            {"role": "system", "content": (
                                         "你是晨报编辑。用户给你今天的文章，每篇含编号、标题和正文。"
                                         "按编号逐篇各写一句话摘要，每篇一行，格式:[1]摘要。"
                                         "只依据正文，不编造正文里没有的内容。"
                                        )},
            {"role": "user",    "content": content}
            ])

    # —— 第4块：取出回答 return（Day17：response.choices[0].message.content）——
    # return ...
    text = response.choices[0].message.content
    parts = re.split(r'\[\d+\]\s*', text)
    return [x.strip() for x in parts if x.strip()]


if __name__ == "__main__":
    # 临时假数据，单独跑这个文件验证（省得联网 fetch）
    fake = [
        {"title": "如何阅读 RSS 源", "link": "x","body":"a"},
        {"title": "Python 虚拟环境入门", "link": "y","body":"b"},
        {"title": "我的周刊第 300 期", "link": "z","body":"c"},
    ]
    print(summarize(fake))
