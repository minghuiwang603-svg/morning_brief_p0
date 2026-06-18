import os
from dotenv import load_dotenv
from openai import OpenAI


def summarize(articles: list) -> str:
    # —— 第1块：把所有标题拼成一段文本 ——
    # for 遍历 articles，把每个 article["title"] 接进一个字符串，每个后面加 "\n"
    # （你写）
    content=""
    for article in articles:                 
       content += article["title"] + "\n" + article["body"] + "\n\n"
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
            {"role": "system",  "content": ("你是一个晨报编辑。"                          
                                     "用户会给你今天几篇文章的标题，每行一篇。"     
                                     "请把它们概括成一段今日导读,要求内容翔实,能让读者知道文章大概讲的是什么"                
                                     "不要逐条复述标题，不要回答标题里的问题。"   
                                     "必须覆盖给你的每一条标题，一条都不能落下、不许编造标题外的内容"
                                     "只能依据标题本身，不要添加标题里没有的内容/细节"   
                                    )}, 
            {"role": "user",    "content": content}
            ])

    # —— 第4块：取出回答 return（Day17：response.choices[0].message.content）——
    # return ...
    return response.choices[0].message.content


if __name__ == "__main__":
    # 临时假数据，单独跑这个文件验证（省得联网 fetch）
    fake = [
        {"title": "如何阅读 RSS 源", "link": "x"},
        {"title": "Python 虚拟环境入门", "link": "y"},
        {"title": "我的周刊第 300 期", "link": "z"},
    ]
    print(summarize(fake))
