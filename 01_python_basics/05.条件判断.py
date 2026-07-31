#if判断格式
#if 条件：
#   操作
from unittest import case

# num = 0
# if num >= 10:
#     print("这个数字>=10")
#     print("hello")
# print("hello")
#
# #案例  完成登录功能（正确账号密码为1888/666888）
# account = input("请输入您的账号：")
# password = input("请输入您的密码：")
# ok_account = "1888"
# ok_password = "666888"

# if account == ok_account and password == ok_password:
#     print("登陆成功")
# if account != ok_account or password != ok_password:
#     print("登录失败")

#if...else...结构
#if 条件：
#   操作
#else:
#   操作

# if account == ok_account and password == ok_password:
#     print("ok")
# else:
#     print("fail")
#
# #案例 根据输入的年份，判断是闰年还是平年  非整百且可以被4整除，整百必须被400整除才是闰年
# year = input("请输入年份;")
# if ( int(year) % 100 != 0 and int(year) % 4 == 0 ) or (int(year) % 100 ==0 and int(year) % 400 == 0 ):
#     print("该年是闰年")
# else:
#     print("该年是平年")
#
# years = int(input("请输入年份："))
# if years % 400 == 0 or years % 4 ==0 and years % 100 != 0:
#     print("该年是闰年")
# else:
#     print("该年是平年")
#
#match...case
# day = int(input("今天是周几:"))
# match day:
#     case 1:
#         print("今天是周一")
#     case 2:
#         print("今天是周二")
#     case 3:
#         print("今天是周三")
#     case 4:
#         print("今天是周四")
#     case 5:
#         print("今天是周五")
#     case 6 | 7:
#         print("今天是周末")
#     case _:
#         print("输入错误")

#实现一个计算器,可以实现+ - * / 运算,用户输入两个数以及运算符之后就可以进行运算
a = float(input("a ="))
b = float(input("b ="))
s = input("s =")
match s:
    case "+":
        print(f"a+b={a} {s} {b} = {a+b}")
    case "-":
        print(f"a-b={a} {s} {b} = {a-b}")
    case "*":
        print(f"a*b={a} {s} {b} = {a*b}")
    case "/":
        if b == 0:
            print("除数不能为0")
        else:
            print(f"a/b={a} {s} {b} = {a/b}")

    case _:
        print("运算符错误")

# 请你编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应的动作(输出控制台)。
# 具体规则：
#   - 上 / w /W             角色向上移动
#   - 下 / s / S              角色向下移动
#   - 左 / a / A             角色向左移动
#   - 右 / d / D             角色向右移动
#   - 跳 / " "(空格)        角色跳跃
#   - 攻击 / j / J            角色发动攻击
#   - 退出 / esc / ESC    角色退出游戏

# up = input("上:")
# down = input("下:")
# light = input("左:")
# right = input("右:")
# jump = input("跳:")
# do = input("攻击:")
# esc = input("退出:")
# match up:
#     case "上"|"w"|"W":
#         print("角色向上移动")
instruction = input("输入指令:")
match instruction:
    case "上"|"w"|"W":
        print("角色向上移动")
    case "下"|"s"|"S":
        print("角色向下移动")
    case "左"|"a"|"A":
        print("角色向左移动")
    case "右"|"d"|"D":
        print("角色向右移动")
    case "跳"|" ":
        print("角色跳跃")
    case "攻击"|"j"|"J" :
        print("角色攻击")
    case "退出"|"esc"|"ESC":
        print("角色退出游戏")
    case _:
        print("指令错误")
