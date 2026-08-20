import os

import json

# import streamlit as st
# import json
#
# if "message" not in st.session_state:
#     st.session_state.message = []
#
# delete = st.button("清空对话")
# if st.button("保存对话"):
#     with open("resources/message.json", "w",encoding="utf-8") as f:
#         json.dump(st.session_state.message, f, ensure_ascii=False, indent=4)
#
# if delete:
#     st.session_state.message = []
#     st.write(f"清空成功")
#
# if st.button("加载对话"):
#     if os.path.exists("resources/message.json"):
#         with open("resources/message.json", "r",encoding="utf-8") as f:
#             st.session_state.message = json.load(f)
#             st.rerun()
#     else:
#         st.write("文件不存在")
#
#
# question = st.chat_input("输入问题")
# if question:
#     st.session_state.message.append({"role": "user", "content": question})
#     st.session_state.message.append({"role": "assistant", "content": f"已收到: {question}"})
# for message in st.session_state.message:
#     st.chat_message(message["role"]).write(message["content"])

session_dict = {}
if os.path.exists('sessions'):
    file_list = os.listdir('sessions')
    for file in file_list:
        try:
            if file.endswith('.json'):
                with open(f"sessions/{file}","r",encoding="utf-8") as f:
                    session_data = json.load(f)
                    session_dict[file[:-5]] = len(session_data["message"])
        except Exception:
            print(f"{file}文件损坏")
    for session_name in sorted(session_dict,reverse=True):
        print(f"{session_name} 消息数: {session_dict[session_name]}")
    print(f"有效会话总数: {len(session_dict)}")
else:
    print(f"有效会话总数: {len(session_dict)}")

