import streamlit as st
import os
from openai import OpenAI
st.set_page_config(
    page_title="AI智能搭档",
    page_icon="🧊",
    #布局
    layout="wide",
    #侧边栏
    initial_sidebar_state="expanded",
    #右上角菜单
    menu_items={
    }
)

#大标题
st.title("AI智能搭档")

#logo
st.logo("resources/logo.png")

#系统提示词
system_prompt = "你是AI助理,你叫小鲸鱼"

#初始化聊天信息
if "message" not in st.session_state:
    st.session_state.message = []

#展示聊天信息
for message in st.session_state.message:    #{"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),
                base_url="https://api.deepseek.com")

#消息输入框
prompt = st.chat_input("请输入要问的问题")
if prompt:  #字符串会自动转换为bool值,如果非空就为True
    st.chat_message("user").write(prompt)
    #保存有输入的提示词
    st.session_state.message.append({"role": "user", "content": prompt})

    #调用大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content":system_prompt },
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "disabled"}}
    )
    #大模型返回的结果
    st.chat_message("assistant").write(response.choices[0].message.content)
    #保存大模型返回的结果
    st.session_state.message.append({"role": "assistant", "content": response.choices[0].message.content})
