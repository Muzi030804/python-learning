from lxml import html

with open("resources/仙逆人物志.html","r",encoding="utf-8") as f:

    html_text = f.read()

    #解析html的文本, 将其转换为一个文档对象
    doc = html.fromstring(html_text)

    #解析表头
    th_list = doc.xpath("//table/thead/tr/th/text()")
    print(th_list)      #['姓名', '性别', '头像', '修为', '技能', '身份地位', '师承', '法宝']

    #解析表格中的数据
    #解析第一行数据
    # td_list = doc.xpath("//table/tbody/tr[1]/td/text()")    # tr[n] 表示表格的第n行
    # print(td_list)

    #解析所有行数据
    tr_list = doc.xpath("//table/tbody/tr")
    for tr in tr_list:
        td_list = tr.xpath("./td/text()")
        print(td_list)