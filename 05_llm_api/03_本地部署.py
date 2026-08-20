import os
from openai import OpenAI

# 创建与本地 Ollama 交互的客户端
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)

#与AI大模型进行交互
response = client.chat.completions.create(
    model="qwen2.5:3b",
    messages=[
        {"role": "system", "content": "你是AI助理,你叫小鲸鱼"},
        {"role": "user", "content": "12个苹果,3个人,怎么均分"},
    ],
    # stream=False
    stream=True
)

# print(response.choices[0].message.content)

#流式输出
full_response = ""
for chunk in response:
    if chunk.choices[0].delta.content:
        content = chunk.choices[0].delta.content
        full_response +=content
        print(content, end="", flush=True)
