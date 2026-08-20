import streamlit as st

import streamlit as st

#页面配置项
st.set_page_config(
    page_title="Streamlit 测试",
    page_icon="🧊",
    #布局
    layout="wide",
    #侧边栏
    initial_sidebar_state="expanded",
    #右上角菜单
    menu_items={
        'Get Help': 'https://chatgpt.com/',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
#标题
st.title("Streamlit 大标题")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

#段落文字
st.write("布偶猫常被称作“猫中仙女”，这源于它那令人过目不忘的出众外貌。它们拥有如蓝宝石般深邃明亮的大眼睛，以及柔软蓬松、触感如丝绸的中长毛。其最标志性的特征便是重点色被毛，身体颜色较浅，而面部、耳朵、四肢和尾巴则呈现深色，形成了优雅的渐变对比，整体气质高贵而温婉。")
st.write("然而，布偶猫真正的魅力更在于其温顺如小狗般的性格。它们天性友善，对人类充满信任，是绝佳的家庭伴侣。布偶猫非常喜欢与人互动，常常会像跟屁虫一样跟随主人，并主动跳上膝盖寻求爱抚，因此获得了“小狗猫”的昵称。它们优雅包容，通常能与其他宠物和孩子和睦相处，是家庭中温柔安静的一员。")
st.write("值得一提的是，布偶猫是一种需要悉心照料的“室内精灵”。它们属于晚熟品种，需要三到四年才能完全展现出成年后的壮美体态。由于是长毛猫，定期的梳毛护理必不可少，以防毛发打结。它们纯粹依赖人类的爱与陪伴，不适合在户外散养。如果用一个词来概括布偶猫，那便是“完美的伴侣”，它们用一生的温柔陪伴，回报主人的精心呵护。")

#图片
st.image("./resources/cat.jpg")

#音频
st.audio("./resources/news.mp3")

#视频
st.video("./resources/news.mp4")

#logo   出现在左上角
st.logo("./resources/logo.png")

#表格
students_data = {
    "姓名":["张三","李四","王五"],
    "学号":[2026001,2026002,2026003],
    "年龄":[18,22,19]

}
st.table(students_data)

#输入框
#普通输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为:{name}")
#密码输入框
password = st.text_input("请输入密码",type="password")
st.write(f"输入的密码为:{password}")

#单选按钮
gender = st.radio("输入性别",["男","女","未知"],index=2)
st.write(f"你的性别为:{gender}")