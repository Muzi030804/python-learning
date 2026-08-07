#字典
# 字典(dict),里面存储的是键值对(key: value)类型的数据,可以根据键(key)找到对应的值(value)
# 特点:以键值对(key: value)形式存储   键(key)不能重复,可修改
# 注意:字典(dict)中的value可以是任何类型的数据,而key不能为可变类型(如:列表,集合,字典),不可变类型有int,float,string,tuple
#定义:    字典名称 = {key: value,key: value,key: value...}
#key不能重复,如果重复不会报错,但后面的会把前面的覆盖
# dict1 = {"a": 1, "b": 2, "c": 3, "a": 4}
# print(dict1)        #{'a': 4, 'b': 2, 'c': 3}
# print(type(dict1))  #<class 'dict'>
# dict1 = {(1,2): 1, 100: 2, 3.14: 3, "a": 4}
# print(dict1)        #{(1, 2): 1, 100: 2, 3.14: 3, 'a': 4}    不可变类型有int,float,string,tuple
# # dict1 = {[1,2]: 1, 100: 2, 3.14: 3, "a": 4}   报错:cannot use 'list' as a dict key  因为list是可变类型
#
# #定义空字典  字典名称 = {}   字典名称 = dict()
# dict2 = {}
# dict3 = dict()
# print(dict2)        #{}
# print(type(dict2))  #<class 'dict'>
# print(dict3)        #{}
# print(type(dict3))  #<class 'dict'>
#
# #根据key获取value
# print(dict1["a"])      #4
# dict1["a"] = 100
# print(dict1["a"])       #100   可以修改
from os import name

# dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# #查询
# print(dict1.get("c"))       #3
# print(dict1["c"])           #3
#
# print(dict1.keys())         #dict_keys(['a', 'b', 'c', 'd'])
# print(dict1.values())       #dict_values([1, 2, 3, 4])
# print(dict1.items())        #dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
#
# #删除
# num = dict1.pop("c")        #有返回值
# print(num)                  #3
# print(dict1)                #{'a': 1, 'b': 2, 'd': 4}
#
# del dict1["d"]              #无返回值
# print(dict1)                #{'a': 1, 'b': 2}
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")       #a: 1  (中间换行) b: 2
# for item in dict1.items():          #item是元组('a', 1)    ('b', 2)
#     print(f"{item[0]}: {item[1]}")  #a: 1  (中间换行) b: 2
# for k, v in dict1.items():          #解包然后遍历
#     print(f"{k}: {v}")              #a: 1  (中间换行) b: 2


# 案例
# 开发购物车管理系统,实现商品信息的增删改查功能,系统使用字典结构存储商品数据,通过控制台菜单与用户交互,具体功能如下
# 1.添加购物车:用户根据提示录入商品名称以及该商品的价格,数量保存该商品信息到购物车
# 2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格,数量,输入完成后修改该商品信息
# 3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品
# 4.查询购物车:将购物车中的商品信息展示除了,格式为:"商品名称: xxx,商品价格: xxx,商品数量: xxx"
# 5.退出购物车

#购物车数据
#shopping_cart = {"商品1":{"price":200,"num":2},"商品2":{"price":100,"num":1}...}
shopping_cart = {}
#控制台菜单
print("##########购物车系统##########")
print("#        1.添加购物车        #")
print("#        2.修改购物车        #")
print("#        3.删除购物车        #")
print("#        4.查询购物车        #")
print("#        5.退出购物车        #")
print("############################")
valid_choose = ["1", "2", "3", "4", "5"]

while True:
    choose = input("请选择要执行的操作(1~5):")
    if choose not in valid_choose:
        choose = input("输入无效,请输入1~5:")
        continue
    match choose:
        #添加购物车功能
        case "1":
            name = input("请输入要录入的商品:")
            if name not in shopping_cart.keys():
                price = float(input("请输入该商品价格:"))
                num = int(input("请输入购买数量:"))
                shopping_cart[name] = {"price": price, "num": num}
            else:
                print("该商品已存在")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        #修改购物车
        case "2":
            name = input("请输入要修改的商品:")
            if name in shopping_cart.keys():
                price = float(input("请输入该商品价格:"))
                num = int(input("请输入购买数量:"))
                shopping_cart[name] = {"price": price, "num": num}
            else:
                print("该商品不存在")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        #删除购物车
        case "3":
            name = input("请输入要删除的商品:")
            if name in shopping_cart.keys():
                del shopping_cart[name]
                print(f"{name}已删除")
                print(f"当前购物车:{shopping_cart}")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        case "4":
            #查询购物车
            for name,msg in shopping_cart.items():
                print(f"商品名称:{name},商品价格:{msg.get("price")},商品数量为:{msg.get("num")}")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        case "5":
            print("已退出系统")
            break
print(shopping_cart)







