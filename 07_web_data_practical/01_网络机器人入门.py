import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求, 获取数据    GET方式而不是POST, 浏览器地址栏发送的请求全都是GET
response = requests.get(target_url)

# 输出数据到控制台  response是一个对象
# print(response.text)
document = html.fromstring(response.text)

#解析数据
#解析表头
th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(th_list)

# 解析表格中的数据
tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)