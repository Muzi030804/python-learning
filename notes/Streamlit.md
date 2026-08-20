## Streamlit基础用法

### 1.标题title

使用 `st.title()` 可以设置标题内容。

```Python
import streamlit as st

st.title('Python从入门到大神')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NDJlZTNiNjZhYjM2ODMwNGVhOTY5ZWU0NGVjZDFkZmNfREduVXBJc0hUb0hheWRRb3BqZUJhejRDWlptZll0ajlfVG9rZW46WnZPQWJuZm1Ib0VUckV4UThscGN6endPbkRlXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 2.段落write

段落就是 `HTML` 里的 `<p>` 元素，在 `streamlit` 里使用 `st.write('内容')` 的方式去书写。

```Python
import streamlit as st

st.write('Hello')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NjgyZWRiMDIyMTQ1NGE4MDQ2NGQ1YmI2NjEwYzQxZDFfcGNKVGNQcUU4N2luZEpUUThJTXpnTjRKTWpmNlBNWjlfVG9rZW46VFA2ZmJhT0Fnb3d6QmR4ZWlxY2NNTXgybnRoXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 3.使用markdown

`streamlit` 是支持使用 `markdown` 语法来写页面内容的，只需使用单引号或者双引号的方式将内容包起来，并且使用 `markdown` 的语法进行书写，页面就会出现对应样式的内容。

```Python
import streamlit as st

"# 1级标题"
"## 2级标题"
"### 3级标题"
"#### 4级标题"
"##### 5级标题"
"###### 6级标题"
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NDczOTBlOTE2NzU0ZTViNTZkNzJkODA4ODA0N2ViNzJfTWlsUHdLSnVWbmEzZk5aV3RScHI2WWRwazJvZFNtSFRfVG9rZW46UkI2dWI0Tk4yb2V4bVZ4dnkyd2NJaXJxbkVkXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 4.图片image

渲染图片可以使用 `st.image()` 方法，也可以使用 `markdown` 的语法。

`st.image(图片地址, [图片宽度])` ，其中图片宽度不是必填项。

```Python
import streamlit as st

st.image('./cat.jpg', width=400)
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NmRjYzM3NWMxMjg0NjA5Y2MwN2I3YTY1Nzc1MzczOWRfMGRLVldIREk4cGNIYTY2MkFxaHdFclNrdG9oZDQ2aDFfVG9rZW46WFlaWmJNOWRzb1M1bnF4RmhqcWNxNEo3bmNkXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 5.表格table

静态表格使用 `st.table()` 渲染，出来的效果就是 `HTML` 的 `<table>`。

`st.table()` 支持传入字典等数据。

```Python
import streamlit as st

data = {"姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧", "红蝶", "十三"],
        "学号": ["20230001", "20230002", "20230003", "20230004", "20230005", "20230006", "20230007"],
        "语文": [80, 90, 85, 70, 95, 90, 85],
        "数学": [87, 92, 87, 81, 92, 69, 83],
        "英语": [90, 85, 90, 95, 80, 85, 90],
        "总分": [257, 267, 262, 241, 267, 244, 258]}
st.table(data)
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MDM0ZjgxMWVlOWM3ZTcyMTE3MjU3ZWI4Njg2NGJlMjdfd29vV3QzNEluMUUzU3RCeExGWUpRcTJDTXJ4RGlyblBfVG9rZW46Wkc5c2JLRVllb1RJR2d4UXd0TWNLdVlCbkFmXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 6.分割线divider

分隔线就是 `HTML` 里的 `<hr>` 。在 `streamlit` 里使用 `st.divider()` 方法绘制分隔线。

```Python
import streamlit as st

st.divider()
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MWU4ZGIyZGZkODVlMzY2M2QzZjI5ZmZhOTFhMzc3MzRfaVBJSTg0YTdSUGlLTUV4RUpZaFpqTjNJdDZLT0RRTVFfVG9rZW46Vm1XVmJUNXF1b0x6aFp4WktpZGN3T0V3bkhiXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 7.输入框

知道怎么声明变量后，可以使用一个变量接收输入框的内容。

输入框又可以设置不同的类型，比如普通的文本输入框、密码输入框。

#### 7.1普通输入框 text_input

输入框使用 `st.text_input()` 渲染。

```Python
import streamlit as st

# 输入框
name = st.text_input("请输入你的姓名：")

if name:
    st.write("你好, ", name)
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjhmZjU3ZjM1YTRiNTg4YjBlZGNiYWU4ZmZlZWQ2ODdfUEhHOTlsNHIzeFBERzlSaEZZYWxPY0Iybm04cGZRM0pfVG9rZW46WHFMTGJsTnh2b0syWGd4d1FoVGMzbENqbnpiXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.2密码 text_input

如果要使用密码框，可以给 `st.text_input()` 加多个类型 `type="password"`。

```Python
import streamlit as st

# 密码
password = st.text_input("请输入你的密码：", type="password")

if password:
    st.write(f"你的密码是{password}吗?")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjFmMjFjYWU5MDJkYTM5NWRkZjZkMGNmN2E5MzBjMGZfSWRXZ3MxUUI0NGxEaVhuSFhMVVRRZk9QaVhJWkI0cDVfVG9rZW46TU9nRGJPeEhBbzlzTWp4ODBVU2N5eXdlbjRjXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.3数字输入框 number_input

数字输入框需要使用 `number_input`

```Python
import streamlit as st

age = st.number_input('年龄：')

st.write(f'你输入的年龄是{age}岁')
```

众所周知，正常表达年龄是不带小数位的，所以我们可以设置 `st.number_input()` 的步长为1，参数名叫 `step`。

```Python
# 省略部分代码

st.number_input('年龄：', step=1)
```

这个步长可以根据你的需求来设置，设置完后，输入框右侧的加减号每点击一次就根据你设置的步长相应的增加或者减少。

还有一点，人年龄不可能是负数，通常也不会大于200。可以通过 `min_value` 和 `max_value` 设置最小值和最大值。同时还可以通过 `value` 设置默认值。

```Python
st.number_input('年龄：', value=20, min_value=0, max_value=200, step=1)
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWQyZmJiNzY0YTZlOGQ1MDU1OGM3NGRhZjI1ZjVhMzhfRjdGdEZHQ3RVZ3RRRU9rU0tFWjRseU1CdVdjS0JodEVfVG9rZW46RVZnQmJmTWhob0w3YXZ4NkptRGNuR2hwbndnXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.4多行文本框 text_area

创建多行文本框使用的是 `st.text_area()`，用法和 `st.text_input()` 差不多。

```Python
import streamlit as st

paragraph = st.text_area("多行内容：")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NzdmZjQ2Yzc0YWI5YTE0MmVmMDY2ODQ5NDA0MmNiMDlfdmlqWUxNTldxU0FlV0FHWjN1dEhsaXdoRXd5aUtiOEdfVG9rZW46TXE4bmJWRldHb0o3OGp4WWNlVWNBT25yblVnXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.5复选框 checkbox

很多应用在登录之前需要用户同意某些协议才能使用，如果你网站也需要这个功能的话可以使用复选框 `st.checkbox()` 让用户去勾选。

```Python
import streamlit as st

checked = st.checkbox("同意以上条款")
if checked:
  st.write("同意")
else:
  st.write("不同意")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MGM4Y2ZmNjFkNDRjOThjYzQ2ZWI1ZmY3MzhlMmU0OWRfbklnSTM4cXpTZEFTS1JnTTJqSEtPMDQySURSWEhqT1RfVG9rZW46SHBNWWIwT2oyb0VPYzh4aDdDWGNSUlY3bkRkXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.6单选框 radio

使用 `st.radio()` 可以制作单选按钮，比如让用户选择性别的时候就能派上用场。

```Python
import streamlit as st

# 单选按钮
is_ok = st.radio("密码正确吗? ", ["正确", "错误"], index=1)

if is_ok:
    st.write(f"密码是{is_ok}的")
```

单选按钮也可以使用一个变量来接收结果。

它还支持设置默认值，使用 `index` 参数即可。`index` 的默认值是1，也就是选中下标为 1 的那项。可以根据你的需求自定义设置。

```Python
import streamlit as st

# 单选按钮
is_ok = st.radio("密码正确吗? ", ["正确", "错误"], index=1)

if is_ok:
    st.write(f"密码是{is_ok}的")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NWE0NjdkYzQ3MGVmNTZmMGZmZTlmYTZiY2I0OGRhMDRfeXVGZW9sdVhwT0ZYTUw4RlFJbXBld3BtOVpYS2R4VVhfVG9rZW46TjE4V2IzSlJYb1hKaU54cEpINGNGM1dQbkZnXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.7单选下拉框 selectbox

使用 `st.selectbox()` 可以创建单选下拉框。

用法是：

```Python
import streamlit as st

subject = st.selectbox(
  "意向学科",
  [
    "AI大模型开发",
    "AI智能应用开发",
    "AI嵌入式+机器人开发",
    "AI测试",
    "AI运维"
  ]
)

st.write(f"你喜欢{subject }")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGJmNGRhNTAxOWQyZjA5N2ZkZTBmMTQ2MzNmZDkxZDBfcVdjZjk3b0w4WU5YZldEMXV4Um9XRU1QWk9ZbUd4bkVfVG9rZW46QTdzMGI5OGFLb0VUekt4YWJVTmNFb29mbm9nXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.8多选下拉框 multiselect

使用 `st.multiselect()` 可以创建多选下拉框，用法和 `st.selectbox()` 一样。

```Python
import streamlit as st

subject_list = st.multiselect("意向学科",
  [
    "AI大模型开发",
    "AI智能应用开发",
    "AI嵌入式+机器人开发",
    "AI测试",
    "AI运维"
  ],
  placeholder="请选择意向学科"
)

for subject in subject_list :
  st.write(f"你喜欢{subject}")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MjU0ZTlmMTM5NGZiYzFjYzkwYWNlNzI2NmI5YzA5MmZfSWY1OVhCQ1BBRWQ3M1lmUVM3NTJSblVyY05SZG54UExfVG9rZW46SzRJbmJEbzZpb1BMMHB4N05RZ2NQN2d1bm9kXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.9滑块 slider

可以使用 `st.slider()` 创建滑块元素。它接收的参数和 `st.number_input()` 差不多，也是可以设置提示语、默认值、最大值、最小值以及步长。

```Python
import streamlit as st

# 滑块
temperature = st.slider("模型温度", value=0.8, min_value=0.1, max_value=2.0, step=0.1)

st.write(f"你设定的模型温度是{temperature}")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MmYxYWQyYzJhMzFmNGNjYTA1Mzg4MjAxNzI5ZjlkMWFfRGJiTlZTM0xIcDlxRDNMc1ZsRE1qRm9PZlJKVXhYQUpfVG9rZW46STVRemJQcm5zb2J0UWl4SGxheGNpQ3Mwbjk4XzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.10按钮 button

使用 `st.button()` 创建按钮。它接收一个字符串作为按钮文本，可以将点击结果赋值给一个变量。

```Python
import streamlit as st

submitted = st.button("新建会话")

if submitted:
  st.write(f"新建会话成功啦")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MTkzODQzZDA2NGUyZjQ0ZDFiNDk1M2NkN2M0Y2FlZGNfUlkzNFY4TVFrS0Y3SFVCbzJUeTh6bDdwSXVCS083V2tfVG9rZW46QTJJRGJlVHNjb05BMm94SXQxVGN2dHB3bkFmXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 7.11文件上传 file_uploader

`python` 擅长做数据分析，有时候可能需要上传一个 `csv` 之类的文件分析一下。

在 `streamlit` 中可以使用 `st.file_uploader()` 创建一个文件上传元素。

```Python
import streamlit as st

# 文件上传
uploaded_file = st.file_uploader("上传文件", type=["csv", "json"])

if uploaded_file:
  st.write(f"你上传的文件是{uploaded_file.name}")
```

`st.file_uploader()` 第一个参数是提示文本，然后可以使用 `type` 属性限制用户上传的文件格式。

接收到的文件可以赋值给一个变量，这个变量接收到文件后可以通过 `.name` 属性查看文件名。

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MWZmYmQyNDA3N2RlMWM2OGQzNjVlNmY3MWRmYTJlZmJfbTliYlVESndOZ2U0Q3JMNXM1czRUMHdUaTdxVFowNW9fVG9rZW46Q0xNMmJKN3Fnbzc5VEd4bnJYdWNsQ21HblplXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 8.侧边栏 sidebar

使用 `st.sidebar()` 可以给网页弄个侧边栏。

```Python
import streamlit as st

with st.sidebar:
  search = st.text_input('搜索：')
  
  st.write(f'页面内容，看看搜索了啥：{search}')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MWZiYTRmMDZhYjEyNzJmZTFhMDRmNDFiOTQxY2JlMDFfem4wQkc2d2Nkb0N2Ulk0eE55R2l0ZzdrT2RGS2l5T3pfVG9rZW46VnNlV2J0MGt4b3NEZ294aGFJcGMzWUxpbmRlXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 9.多列布局 columns

按照前面学到的内容写页面的话，所有元素都是从上往下布局的。如果你想一个页面有多列布局，可以使用 `st.columns()` 方法。

```Python
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
  st.write('第1列')

with col2:
  st.write('第2列')

with col3:
  st.write('第3列')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGE0MDI1NjdjMjRkODA0YjkyYWViMzFiOGI5ZDYyNGZfRklYQWhienVoNVg2M1NGcFp3SEtFTks4TXRjZGpkeDFfVG9rZW46Q05rZmJVRWpzb2dkVXl4YW9TY2NJYVlZbnBnXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

在使用 `st.columns` 时，默认每列的宽度都是一样的。如果你希望每列宽度占比不一样的话可以这样写。

```Python
import streamlit as st

# 多列布局（不同比例）
col1, col2, col3 = st.columns([1, 2, 3])

with col1:
  st.write('第1列')

with col2:
  st.write('第2列')

with col3:
  st.write('第3列')
```

此时 `st.columns()` 括号里传入的就不是数字（列数），而是一个数值型列表，这个列表元素个数表示列数，元素的数字表示每列占比。

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MDBhMGMyZmQyMjVmMWU3ZDllMDhjMGQzM2E1NzAxNDBfb1pGdXBaVTlpUXJBZUU3UTdjN2dBVUJmdThmaEVHMGVfVG9rZW46RUJBVmJIT3Fmb21xaHF4Y3F6WWNhZnB4bnpiXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 10.选项卡 tabs

使用 `st.tabs()` 可以创建选项卡组件。

```Python
import streamlit as st

# 选项卡
tab1, tab2, tab3 = st.tabs(['点赞', '关注', '收藏'])

with tab1:
  st.write('快点赞吧')
with tab2:
  st.write('关注一下啦')
with tab3:
  st.write('收藏就是学会了')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=MGEyYjIyODdmNzJlMmI0MjY5NGM1ZGM5YWJlOWRkNjJfM1V5eXM1ZFRCU2hTcjJxNGx4ZGVYVnF2V1dJekszam1fVG9rZW46RUQ0MWJSSWFWb2Z3bGV4aXBlbmN6dHREbkJnXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 11.折叠展开组件 expander

使用 `st.expander()` 可以创建折叠展开组件。

```Python
import streamlit as st

with st.expander('更多信息'):
  st.write('传智教育')
  st.write('博学谷')
  st.write('黑马程序员')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjU4YTY4ZWE2M2E2NDc4NmQ3Y2VhOTAyYzQ4YTc5MmJfTFQxYTJQVnF5a1JVUHNHWHVtSE1LWkxKeGxRRnhxZ21fVG9rZW46TXJLNGJDakJ1b0p6bEF4SGFsOGNrcGV5bmdnXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 12.扩展：音视频组件

#### 12.1logo

如果你想在页面中，增加一个logo图标，可以使用`st.logo`进行实现。

```Python
import streamlit as st

st.logo('./logo.png')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmNmM2RkNTUzNDA5NGZmNmIwMTBjY2UyZmVlZWNkNGZfaUNRd2tDSDYyYTdxU3JuQXBWUjdoZGhiYlFQbWFVR2NfVG9rZW46Vk5XY2JJdmczb29yNzR4RmlsVmMxWEVUbmlmXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 12.2音频标签 audio

```Python
import streamlit as st

st.audio('./01.mp3', format='audio/mp3')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=OWMyNjJmM2M4ZWNjZTdlNzM2MmViYzE4ZDM3MjJlZjVfb1Y2ZEh3QTRPMWV3YmpITFk3TWczNGpxWEF5bk95V2NfVG9rZW46UFJUR2JybGRHb0J3ekh4cVY2SmNzSEhtblZnXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 12.3视频标签 video

```Python
import streamlit as st

st.video('./01.mp4', format='video/mp4')
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NWRlMTg2ZmRlYzdlOTdkYWE0YWU1YjJkNDU0NTQyZjJfZDlYMGE3TENaRE9sNjZLcExZR1E2dlRMemFsckpvQ1hfVG9rZW46WEJpWWJKbktQb1JIUmJ4VEM1cGNnZTM5blljXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 13聊天元素

#### 13.1Chat文本输入框 chat_input

```Python
import streamlit as st

prompt = st.chat_input("请输入您想问的问题")
if prompt:
    st.write(f"您输入的问题为: {prompt}")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NWYzMzZiMGQwMWZkZjk1YmRlMDY2Zjg2NjM0MzM2MTdfZ1laenNFWFpYU0dLaUdvZzk4VWc2eUtScDBlWGN5aUZfVG9rZW46UWxhVmJJblFSb2hLSmp4SkhvRWNENGRFblpjXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

#### 13.2Chat消息 chat_message

```Python
import streamlit as st

# 用户信息
with st.chat_message("user"):
    st.write("Hello 👋")
    
# 机器人信息
message = st.chat_message("assistant")
message.write("Hello human")
```

效果:

![img](https://heuqqdmbyk.feishu.cn/space/api/box/stream/download/asynccode/?code=NThlOTRiYzJlMTYwYTk1MzU4ZGEyMGZhY2ViMzQ1MjVfcXZIYWtGN2V4Z1hjcUpEUm1hY2Fua21lN1lwck5pN2hfVG9rZW46SElpZGJ0NVdTb1BSVVF4cWdLeGNCWFdxbmtiXzE3ODY2OTU2MzM6MTc4NjY5OTIzM19WNA&add_watermark=true&scene_type=CCM)

### 14.会话状态 session_state

#### 14.1 st.session_state的作用

Streamlit 每次用户进行交互时，都会**从上到下重新运行整个 Python 脚本**。

普通变量会重新创建，例如：

```
count = 0
count += 1
```

每次重新运行：

```
count → 又变成 0
```

如果希望一个变量在多次重新运行之间继续保存，就可以使用：

```
st.session_state
```

例如：

```python
import streamlit as st


if "count" not in st.session_state:
    st.session_state.count = 0


if st.button("加1"):
    st.session_state.count += 1


st.write(st.session_state.count)
```

这里：

```
if "count" not in st.session_state:
```

表示：

> 如果当前会话中还没有 `count`，第一次运行时创建它。

所以不会因为 Streamlit 重新运行脚本就把 `count` 重置为 `0`。

------

#### 14.2 两种访问方式

`session_state` 可以理解成一个特殊的字典。

#### 方式一：属性形式

```
st.session_state.count = 0


print(st.session_state.count)
```

#### 方式二：字典形式

```
st.session_state["count"] = 0


print(st.session_state["count"])
```

两者作用基本相同。

------

#### 14.3 初始化 session_state

通常不要直接写：

```
st.session_state.message = []
```

因为 Streamlit 每次重新运行脚本都会执行这一句，会导致历史数据被清空。

应该写：

```
if "message" not in st.session_state:
    st.session_state.message = []
```

含义是：

```
message不存在
      ↓
创建 message = []


message已经存在
      ↓
保持原来的内容
```

------

#### 14.4 使用 session_state 保存聊天记录

典型的例子：

```
if "message" not in st.session_state:
    st.session_state.message = []
```

用户输入后保存：

```
st.session_state.message.append(
    {
        "role": "user",
        "content": prompt
    }
)
```

AI回答后保存：

```
st.session_state.message.append(
    {
        "role": "assistant",
        "content": response
    }
)
```

最终：

```
st.session_state.message
```

可能保存：

```
[
    {
        "role": "user",
        "content": "你好"
    },
    {
        "role": "assistant",
        "content": "你好，我是小鲸鱼"
    },
    {
        "role": "user",
        "content": "你叫什么名字？"
    }
]
```

因此可以使用：

```
for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])
```

把之前的聊天记录重新显示出来。

------

#### 14.5st.session_state与普通变量的区别

| 普通变量               | `st.session_state`              |
| ---------------------- | ------------------------------- |
| 脚本重新运行后重新创建 | 可以跨 rerun 保存               |
| `message = []`         | `st.session_state.message = []` |
| 适合临时计算           | 适合保存页面状态                |
| 无法直接保存聊天上下文 | 适合保存聊天记录                |

> **`st.session_state` 用于在 Streamlit 脚本多次 rerun 之间保存当前用户会话的数据。**