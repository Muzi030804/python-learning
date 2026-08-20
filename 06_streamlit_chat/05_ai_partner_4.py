"""
会话管理
"""

import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

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

# 保存会话信息函数
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "message": st.session_state.message
        }

        # 如果sessions文件不存在,则创建
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)

#生成会话标识(用当前时间表示)
def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#加载所有会话列表信息
def load_sessions():
    session_list = []
    # 加载sessions目录下的文件  拿到sessions目录下的所有文件,再依次处理单个文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")      #file_list里是文件名形成的列表 ,比如 2026-08-17_17-22-48.json
        for filename in file_list:
            if filename.endswith(".json"):      #如果是以.json结尾
                session_list.append(filename[:-5])    #会话列表名称只保留日期,不保留后面的.json,比如2026-08-17_17-22-48,2026-08-17_17-22-48.json倒数第五个字符是.
    session_list.sort(reverse=True)
    return session_list

#加载指定会话信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.message = session_data["message"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception:
        st.error("会话加载失败")

# 删除会话信息
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            #如果删除的是当前会话,则需要到新页面
            if session_name == st.session_state.current_session:
                st.session_state.message = []
                st.session_state.current_session = generate_session_name()
    except Exception:
        st.error("删除会话失败")

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


# 初始化聊天信息    定义st.session_state.message用来存储所有的{"role":..,"content":...}信息
if "message" not in st.session_state:
    st.session_state.message = []
# 昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小鲸鱼"
# 性格
if "nature" not in st.session_state:
    st.session_state.nature = "一丝不苟,冷酷无情"
# 会话标识 (用当前时间表示)
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

#展示聊天信息
st.text(f"会话名称{st.session_state.current_session}")
for message in st.session_state.message:    #{"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),
                base_url="https://api.deepseek.com")

# 侧边栏    with:streamlit中的上下文管理器,创建一个侧边栏,这样之后的代码会自动加上with内容
with st.sidebar:
    #会话信息
    st.subheader("AI控制面板")

    #新建会话
    if st.button("新建会话",width="stretch",icon="✏️"):
        #1.保存当前会话信息
        save_session()

        #2.创建会话
        if st.session_state.message:    #如果聊天信息非空,则保存当前对话信息
            st.session_state.message = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun() #重新运行当前页面,清除原来渲染的页面

    #会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            if st.button(session,width="stretch",icon="📄",key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            #删除会话信息
            if st.button("",width="stretch",icon="❌️",key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
    # 分隔线
    st.divider()

    # 助手信息
    # st.sidebar.subheader("助手信息")   不使用with的情况下
    # nick_name = st.sidebar.text_input("昵称")
    st.subheader("助手信息")
    #昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
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

    #保存会话信息
    save_session()
