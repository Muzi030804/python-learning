"""
增加侧边栏
"""

import streamlit as st
import os
from openai import OpenAI
st.set_page_config(
    page_title="AI助手",
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
st.title("AI助手")

#logo
st.logo("resources/logo.png")

#系统提示词
system_prompt = """
        你是AI助理,你叫%s
        规则:
        1.每次只回一条信息
        2.匹配用户的语言
        3.回复简短
        4.用符合风格的方式对话
    风格:
        %s
    必须严格遵守以上规则进行回复
"""


#初始化聊天信息    定义st.session_state.message用来存储所有的{"role":..,"content":...}信息
if "message" not in st.session_state:
    st.session_state.message = []
# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小鲸鱼"
#性格
if "nature" not in st.session_state:
    st.session_state.nature = "一丝不苟,冷酷无情"

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

#侧边栏    with:streamlit中的上下文管理器,创建一个侧边栏,这样之后的代码会自动加上with内容
# st.sidebar.subheader("助手信息")
# nick_name = st.sidebar.text_input("昵称")
with st.sidebar:
    st.subheader("助手信息")
    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    nature = st.text_area("风格",placeholder="请输入风格",value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

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
            {"role": "system", "content":system_prompt %(st.session_state.nick_name,st.session_state.nature) },
            # {"role": "user", "content": prompt},
            # 解包st.session_state.message  把模型输入换为st.session_state.message的内容,st.session_state.message是包含{"role":..,"content":...}的列表
            *st.session_state.message,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "disabled"}}
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
