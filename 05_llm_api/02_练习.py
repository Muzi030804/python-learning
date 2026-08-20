
"""
#今日唯一代码练习：编写函数parse_response(response)，
# 从模拟的大模型响应字典中取出choices里第一条message的content和usage中的total_tokens，并以元组返回。
# 输入示例：{"choices":[{"message":{"role":"assistant","content":"你好"}}],"usage":{"total_tokens":37}}；
# 预期结果：("你好", 37)。
# 验收：必须使用函数、参数、返回值和字典/列表访问；不得写死“你好”和37；
# 再更换内容及token数测试；不要调用真实API或写入密钥。
# import os
#
# from openai import OpenAI
#
# client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")
#
# response = client.chat.completions.create(
#     model = "deepseek-v4-pro",
#     messages=[
#         {"role": "system", "content": "你是AI助理,你叫小鲸鱼"},
#         {"role": "user", "content": "你好"}
#     ],
#     stream=False
# )

"""

response = {"choices":[{"message":{"role":"assistant","content":"你好"}}],"usage":{"total_tokens":37}}
response1 = {"choices":[{"message":{"role":"assistant","content":"你能做什么"}}],"usage":{"total_tokens":188}}
#从模拟的大模型响应字典中取出choices里第一条message的content和usage中的total_tokens，并以元组返回。
# def parse_response(response):
#     re = response.choices[0].message.content
#     usage = response.usage.total_tokens
#     return (re, usage)
def parse_response(response):
    llm_response = response["choices"][0]["message"]["content"]
    usage = response["usage"]["total_tokens"]
    return (llm_response, usage)

print(parse_response(response))
print(parse_response(response1))
