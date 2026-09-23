from lxml import html


#读取html文件
with open("resources/仙逆人物志.html","r",encoding="utf-8") as f:
    html_text = f.read()

    #解析html的文本, 将其转换为一个文档对象
    document = html.fromstring(html_text)

    #解析表头
    # /table/thead/tr/th/text() : 表示从根节点开始匹配
    # th_list = document.xpath("/html/body/div/div/table/thead/tr/th/text()")
    # //table/thead/tr/th/text() : 表示从任意位置开始匹配

    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list)      #['姓名', '性别', '头像', '修为', '技能', '身份地位', '师承', '法宝']

    # tr[2] : 表示匹配第2个tr标签
    td_list = document.xpath("//table/tbody/tr[2]/td/text()")
    print(td_list)      #['李慕婉', '女', '元婴期', '冰系神通、寒气凝霜', '天逆宗长老', '家族传承', '寒冰玉镯、雪蚕丝袍']

    # last() : 表示匹配最后一个
    td_list = document.xpath("//table/tbody/tr[last()-1]/td/text()")    #last()-1 : 倒数第二个
    print(td_list)      #['十三', '男', '筑基初期', '隐匿追踪、暗杀之术', '神秘杀手', '未知', '暗影匕首、隐身符']

    # p[@class] : 表示匹配class的p标签
    p_list = document.xpath("//p[@class]/text()")
    print(p_list)       #['探索修真世界的奥秘，记录修仙路上的传奇']

    # p[@class='xn'] : 表示匹配class且属性为xn的p标签
    p_list = document.xpath("//p[@class='xn']/text()")
    print(p_list)       #['探索修真世界的奥秘，记录修仙路上的传奇']

    # * : 表示匹配任意标签
    th_list = document.xpath("//table/thead/tr/*/text()")   #//table/thead/tr下的所有标签
    print(th_list)      #['姓名', '性别', '头像', '修为', '技能', '身份地位', '师承', '法宝']

    # @src : 表示匹配src属性
    a_list = document.xpath("//td/img/@src")
    print(a_list)       #['https://ai-web-2025.oss-cn-beijing.aliyuncs.com/1.png', 'https://ai-web-2025.oss-cn-beijing.aliyuncs.com/1.png',.........

    # @* : 表示匹配任意属性
    a_list = document.xpath("//td/img/@*")
    print(a_list)       #['https://ai-web-2025.oss-cn-beijing.aliyuncs.com/1.png', '王林', 'https://ai-web-2025.oss-cn-beijing.aliyuncs.com/1.png', '李慕婉', ............