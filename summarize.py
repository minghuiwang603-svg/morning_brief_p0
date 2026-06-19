import os
from dotenv import load_dotenv
from openai import OpenAI
import re


def clean_html(text):   
    return re.sub(r"<[^>]+>", "", text)
    

def summarize(articles: list) -> str:
    # —— 第1块：把所有标题拼成一段文本 ——
    # for 遍历 articles，把每个 article["title"] 接进一个字符串，每个后面加 "\n"
    # （你写）
    content=""
    for article in articles:                 
        content += article["title"] + "\n" + clean_html(article["body"]) + "\n\n"
    # —— 第2块：造 client（照抄你 Day17 test_llm.py 那三行：load_dotenv / 取 key / OpenAI(...)）——
    # （你写）
    load_dotenv()
    d_key=os.environ.get("DEEPSEEK_API_KEY")
    client = OpenAI(api_key=d_key,base_url="https://api.deepseek.com")
    # —— 第3块：调 DeepSeek，messages 两条 ——
    # response = client.chat.completions.create(
    #     model="deepseek-chat",
    #     messages=[
    #         {"role": "system",  "content": "你写规矩：中文、3句以内、不带链接、口吻像今日导读"},
    #         {"role": "user",    "content": 第1块拼出来的标题文本},
    #     ],
    # )
    response=client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": (
                                         "你是晨报编辑。用户给你今天的文章，每篇含标题和正文。"
                                         "把所有文章概括成一段中文今日导读，3句以内、不超过150字。"
                                         "必须覆盖每一篇，不要逐条复述标题，"
                                         "只依据正文，不编造正文里没有的内容。"
                                        )},
            {"role": "user",    "content": content}
            ])

    # —— 第4块：取出回答 return（Day17：response.choices[0].message.content）——
    # return ...
    return response.choices[0].message.content


if __name__ == "__main__":
    # 临时假数据，单独跑这个文件验证（省得联网 fetch）
    fake = [
        {"title": "如何阅读 RSS 源", "link": "x","body":"a"},
        {"title": "Python 虚拟环境入门", "link": "y","body":"b"},
        {"title": "我的周刊第 300 期", "link": "z","body":"c"},
    ]
    print(summarize(fake))
