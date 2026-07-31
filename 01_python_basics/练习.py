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
n = int(input("请输入一个正整数:"))
m = 1
num = 0
sum = 0
while m <= n:
    if m % 3 ==0 and m % 5 != 0:
        num += 1
        sum += m
        print(m)
    m += 1
print(f"符合条件的数量：{num}")
print(f"符合条件的总和：{sum}")
