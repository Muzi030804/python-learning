import json

#写入json数据文件
user = {
    "name" : "张三",
    "age" : 18,
    "gender" : "男",
    "hobbies" : ["reading", "swimming"]
}
with open("resources/users.json", "w",encoding="utf-8") as f:
    #ensure_ascii:默认为True,确保所有的数据输出的数据都是ascii编码(非ASCII码会进行转义);False,非ASCII码保留原样输出
    #indent:会在输出的json数据中添加缩进(格式化)
    json.dump(user,f,ensure_ascii=False,indent=4)

#读取json数据文件
with open("resources/users.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))