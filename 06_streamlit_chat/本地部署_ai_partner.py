"""
增加记忆功能
"""

import streamlit as st
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

#初始化聊天信息    st.session_state.message用来存储所有的{"role":..,"content":...}信息
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
client = OpenAI(api_key="ollama",
                base_url="http://localhost:11434/v1/")

#消息输入框
prompt = st.chat_input("请输入要问的问题")
if prompt:  #字符串会自动转换为bool值,如果非空就为True
    st.chat_message("user").write(prompt)
    #保存有输入的提示词
    st.session_state.message.append({"role": "user", "content": prompt})

    #调用大模型
    response = client.chat.completions.create(
        model="qwen2.5:3b",
        messages=[
            {"role": "system", "content":system_prompt },
            #解包st.session_state.message  把模型输入换为st.session_state.message的内容,st.session_state.message是包含{"role":..,"content":...}的列表
            *st.session_state.message,
            # {"role": "user", "content": prompt},
        ],
        stream=True,
    )
    #大模型返回的结果(非流式输出的解析方式)   stream=False
    # st.chat_message("assistant").write(response.choices[0].message.content)

    #大模型返回的结果(流式输出的解析方式)   stream=True
    response_message = st.empty()   #创建一个空组件,用于展示大模型返回的结果,不然就会瀑布式输出

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content
            response_message.chat_message("assistant").write(full_response)     #原来的空组件实时接收流式输出的结果

    #保存大模型返回的结果
    # st.session_state.message.append({"role": "assistant", "content": response.choices[0].message.content})
    st.session_state.message.append({"role": "assistant", "content": full_response})
