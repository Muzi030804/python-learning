#if...elif...else结构
# if 条件1:
#   操作1
#elif 条件2：
#   操作2
#else：
#   操作3

#输入一个数字，判断是正数，负数还是0
# num = int(input("输入一个数："))
# if num > 0:
#     print("正数")
# elif num < 0:
#     print("负数")
# else:
#     print("0")

#根据用户名 密码进行登录 用户名 密码分别为admin/666888,root/111111,zhangsan/123456,否则就提示用户名或密码错误
# name = input("输入用户名:")
# password = input("输入密码:")
# if name == "admin" and password == "666888":
#     print("登陆成功")
# elif name == "root" and password == "111111":
#     print("登陆成功")
# elif name == "zhangsan" and password == "123456":
#     print("登陆成功")
# else:
#     print("用户名或密码错误")

#根据输入的成绩,判断成绩等级 >=85 优秀  60~85 及格  否则不及格
# score = int(input())
# if score >= 85:
#     print("优秀")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")

# 购物折扣计算：根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
#   1. 金额 >= 500: 8折
#   2. 300 <= 金额 < 500: 9折
#   3. 100 <= 金额 < 300: 95折
#   4. 金额 < 100: 无折扣

# total = float(input())
# if total >= 500:
#     print(f"应付金额为:{total*0.8:.2f}")
# elif 300<=total<500:
#     print(f"应付金额为:{total * 0.9:.2f}")
# elif 100<=total<300:
#     print(f"应付金额为:{total * 0.95:.2f}")
# else:
#     print(f"应付金额为:{total}")
#
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
#
# if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("等边三角形")
#     elif a == b or b == c or a == c:
#         print("等腰三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不是三角形")

# 北京市居民年度用电电费计算：根据输入的用电度数，计算电费
# 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
# - 阶梯电价规则：
#   1. 第一档：2880度以下，电费单价0.4883元/度
#   2. 第二档：2880-4800度，电费单价0.5383元/度
#   3. 第三档：4800度以上，电费单价0.7883元/度
# num = float(input("用电度数:"))
# if num < 2880:
#     money = num*0.4883
# elif num < 4800 :
#     money = 2880*0.4883+(num-2880)*0.5383
# else :
#     money = 2880*0.4883+1920*0.5383+(num-4800)*0.7883
# print(f"电费为:{money}")

# 输入一个正整数 n，使用 while 循环找出 1～n 中：
# 能被 3 整除；
# 但不能被 5 整除的数字。
# 依次输出符合条件的数字，最后输出数量和总和。
# 输入示例：
# 请输入正整数：20
# 预期输出：
# 3
# 6
# 9
# 12
# 18
# 符合条件的数量：5
# 符合条件的总和：48
# n = int(input("请输入一个正整数:"))
# m = 1
# num = 0
# sum = 0
# while m <= n:
#     if m % 3 ==0 and m % 5 != 0:
#         num += 1
#         sum += m
#         print(m)
#     m += 1
# print(f"符合条件的数量：{num}")
# print(f"符合条件的总和：{sum}")

# 给定成绩列表：
# [58, 60, 73, 45, 90]
# 使用循环输出所有大于或等于 60 的成绩，最后输出及格人数和及格成绩总和。
# 预期输出：
# 60
# 73
# 90
# 及格人数：3
# 及格成绩总和：223
# 验收标准：
# 必须使用列表、for 循环和条件判断。
# 不能使用内置的 sum()。
# 60 必须算作及格。
# 还要分别测试 [60]、[59] 和空列表 []。
# 只改变列表内容时，统计逻辑不能跟着修改。
# l = [58,60,73,45,90]
# total = 0
# num = 0
# for x in l:
#     if x >=60:
#         num += 1
#         total += x
#         print(x)
# print(f"及格人数为:{num}")
# print(f"及格成绩总和为:{total}")

#用户输入一句英文，将它转换为小写并按空格拆分。删除重复单词，同时保留单词第一次出现的顺序，最后输出去重后的列表和单词数量。
# 输入示例：
# Python is fun and python is useful
# 预期输出：
# ['python', 'is', 'fun', 'and', 'useful']
# 不同单词数量：5
# s = input("输入一句英文:")
# new_s = s.lower().split()
# print(new_s)
# l = []
# num = 0
# for i in new_s:
#     if i not in l:
#         num += 1
#         l.append(i)
# print(f"去重后的列表为:{l}")
# print(f"单词数量为:{num}")

# 给定订单元组：
# (
#     ("A001", "键盘", 2, 199),
#     ("A002", "鼠标", 3, 89),
#     ("A003", "显示器", 1, 1299)
# )
# 每条订单依次表示：订单号、商品名、数量、单价。遍历订单，输出每条订单的小计，最后输出全部订单总额。
# 预期输出：
# A001 键盘 小计：398
# A002 鼠标 小计：267
# A003 显示器 小计：1299
# 订单总额：1964
# 验收标准：
# 订单数据必须保持为元组且不能修改。
# 遍历时使用元组解包取得四个字段。
# 每条订单的小计必须由数量和单价计算，不能直接填写结果。
# 空元组应输出订单总额 0。
# 改变数量或单价后，统计逻辑不需要修改。
# t = (
#     ("A001", "键盘", 2, 199),
#     ("A002", "鼠标", 3, 89),
#     ("A003", "显示器", 1, 1299)
# )
# total = 0
#
# for i in t:
#     print(f"{i[0]} \t {i[1]} \t 小计:{i[2]*i[3]}")
#     total += i[2]*i[3]
#
# print(f"订单总额：{total}")
# #解包,不依赖索引
# orders = (
#     ("A001", "键盘", 2, 199),
#     ("A002", "鼠标", 3, 89),
#     ("A003", "显示器", 1, 1299)
# )
#
# total = 0
#
# for order_id, product_name, quantity, unit_price in orders:
#     subtotal = quantity * unit_price
#     print(f"{order_id}\t{product_name}\t小计：{subtotal}")
#     total += subtotal
#
# print(f"订单总额：{total}")

# i = input()
# s = ["1","2","3","4","5"]
# if i not in s:
#     print("i无效")

#给定列表：
# ["python", "agent", "python", "rag", "agent", "python"]
# # 统计每个单词出现的次数，并保存到一个字典中。
# # 预期结果：
# # {"python": 3, "agent": 2, "rag": 1}
# # 验收标准：
# # 必须通过循环逐个处理列表元素。
# # 必须使用字典保存“单词—次数”。
# # 不能使用 list.count() 或 collections.Counter。
# # 不能修改原列表。
# # 输入空列表时应得到空字典。
# # 列表中增加任何新单词后，统计逻辑不需要修改。
# dict1 = {1: {"ch": 2,"ma":4}, 2: {"ch": 2,"ma":25}, 3: {"ch": 3,"ma":55}}
#
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# l = []
# for key,value in dict1.items():
#     l.append(value["ch"])
# print(l)
# print(dict1[1].values())

# l = [5,4,2,1,1,9,10]
# print(l.index(max(l)))
# print(max(l))

#给定嵌套字典：
# {
#     "键盘": {"price": 199, "stock": 5},
#     "鼠标": {"price": 89, "stock": 0},
#     "显示器": {"price": 1299, "stock": 2}
# }
# 输出每种商品的库存金额，并计算全部库存总额。
# 预期输出：
# 键盘 库存金额：995
# 鼠标 库存金额：0
# 显示器 库存金额：2598
# 全部库存总额：3593
# 验收标准：
# 使用 items() 解包遍历商品名称和商品信息。
# 只能使用一层循环。
# 商品名称必须与同一条记录中的价格、库存对应。
# 库存金额必须动态计算。
# 空字典应输出全部库存总额 0。
# 增删商品后不需要修改统计逻辑。
shopping = {
    "键盘": {"price": 199, "stock": 5},
    "鼠标": {"price": 89, "stock": 0},
    "显示器": {"price": 1299, "stock": 2}
}
total = 0
for name, shop in shopping.items():
    print(f"{name}, 库存金额:{shop["price"] * shop["stock"]}")
    total += shop["price"]* shop["stock"]
print("全部库存总额：",total)
