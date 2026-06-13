import os
from dotenv import load_dotenv


load_dotenv()
d_key=os.environ.get("DEEPSEEK_API_KEY")


from openai import OpenAI
client = OpenAI(api_key=d_key,base_url="https://api.deepseek.com")
response=client.chat.completions.create(model="deepseek-chat",messages=[{"role": "user", "content": "目前马斯克身价多少"}])
print(response.choices[0].message.content)
print(response.usage)
