#打印10遍hello world
# num = 0
# while num < 10:
#     num += 1
#     print(num)
import random

#案例计算1~100中的所有偶数和
# n = 1
# s = 0
# while n <= 100:
#     if n % 2 == 0:
#         s += n
#     n += 1
# print(s)

#for循环结构
#for 元素 in 待处理数据集
#   循环体
#else:
#   循环结束时执行的代码
# msg = "hello world"
# for i in msg:
#     print(i)
# else:
#     print("循环结束")

#计算1~100的奇数和
# total = 0
# for i in range(100):
#     if i % 2 != 0:
#         total += i
# print(total)
# for i in range(1,101,2):
#     total += i
# print(total)

#计算100~500之间所有的3的倍数的数字之和
# num =0
# for i in range(100,501):
#     if i % 3 == 0:
#         num += i
# print(num)

#打印一个长度为m 宽度为n的长方形
# m = int(input("长方形的长为:"))
# n = int(input("长方形的宽为:"))
# for i in range(n):
#     for j in range(m):
#         print("*",end=" ")
#     print()

#打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}",end="\t")
#     print()

#练习1：根据输入的直角边的边长，打印等腰直角三角形 （如下为直角边为5的等腰直角三角形）
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
# n = int(input("等腰直角三角形边长为:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
#练习2：根据输入的数字，打印对应的数字金字塔
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5
# 1   2   3   4   5   6
# 1   2   3   4   5   6   7
# m = int(input("数字金字塔高:"))
# for i in range(m+1):
#     for j in range(1,i+1):
#         print(j, end="\t")
#     print()
# for i in range(m):
#     for j in range(0,i+1):
#         print(j+1, end="\t")
#     print()
# 练习3：打印国际象棋棋盘
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# ■   □   ■   □   ■   □   ■   □
# □   ■   □   ■   □   ■   □   ■
# for i in range(8):
#     for j in range(8):
#         if i % 2 ==0 and j % 2 == 0 or i % 2 ==1 and j % 2 == 1:
#             print("■",end="\t")
#         else:
#             print("□",end="\t")
#     print()

# while True:
#     account = input("输入账号:")
#     password = input("输入密码:")
#
#     if account == "" or password == "":
#         print("用户名和密码不能为空,请重新输入")
#         continue
#
#     if account == "admin" and password == "666888" or account == "zhangsan" and password == "123456":
#         print("登录成功")
#         break
#     print("用户名或密码错误,请重新输入")

#猜数字

# random_number = random.randint(1, 100)  #生成1~100 的随机数
# while True:
#     num  = int(input("猜数字:"))
#     if num == random_number:
#         print(f"猜对了,就是{random_number}")
#         break
#     elif num > random_number:
#         print("猜大了")
#         continue
#     elif num < random_number :
#         print("猜小了")
#         continue
#     else:
#         print("请输入1~100的数字")
#         continue

#需求1：将1-1000之间（含1000）所有的5的倍数的数字累加起来。
# total = 0
# for i in range(1,1001):
#     if i % 5 ==0:
#         total += i
# print(total)
# 需求2：统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
num_a = 0
num_k = 0
for i in s:
    if i =="a":
        num_a += 1
    elif i =="k":
        num_k += 1
print(f"a有{num_a}个")
print(f"k有{num_k}个")
