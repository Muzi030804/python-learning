import os
from openai import OpenAI

#创建与AI大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")  #os.environ拿到系统的环境变量,DEEPSEEK_API_KEY是环境变量的名字,值就是DeepSeek的API key

#与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是AI助理,你叫小鲸鱼"},
        {"role": "user", "content": "12个苹果,3个人,怎么均分"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "disabled"}}
)

#这里的
print(response.choices[0].message.content)  #每人分 **4个苹果**：12 ÷ 3 = 4。如果苹果大小不一，想分得更公平，可以全部切块或榨成汁再平均分成3份。