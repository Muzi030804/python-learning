# 参数与返回值学习记录

#具体格式如下:
#def 函数名(参数列表):
#   函数体
#   ......
#   return 返回值          (可以没有返回值)

#调用函数
#函数名(参数)

#计算圆的面积
# def circle_area(radius):
#     return 3.14 * radius**2
#
# c_area = circle_area(5)
# print(c_area)
#
# #计算长方形的面积
# def rectangle(width, height):   #形参:函数定义时括号里的参数,只能在函数内使用(局部变量)
#     return width * height
#
# r_area = rectangle(5, 6)    #实参:函数在调用时输入的参数
# print(r_area)
#
# #计算圆的面积和周长
# def circle_area_length(radius): #如果返回值有多个,多个返回值之间逗号分隔
#     return round(3.14 * radius**2,1),round(2*3.14*radius,1)         #round(a,b):  让a保留b位小数
# circle_area_len = circle_area_length(5)
# print(circle_area_len)      #(78.5, 31.4)  多个返回值会封装到元组
# print(type(circle_area_len))    #<class 'tuple'>
#
# #解包
# area, length = circle_area_length(5)
# print(area)         #78.5
# print(length)       #31.4

#函数的说明文档
#函数的说明文档(Docstring)是写在函数开头,用三个引号包裹的字符串,用于解释函数的功能  参数  返回值等信息,方便调用者清楚函数的具体作用和细节
# def circle_area(radius):
#     """
#     该函数用于根据圆的半径,计算圆的面积和周长
#     :param radius: 圆的半径
#     :return: 圆的面积,圆的周长
#     """
#     return 3.14 * radius * radius,2*3.14*radius
#
# a = circle_area(5)
# print(a)

#函数的嵌套调用
# 嵌套调用值得是在一个函数中,又调用了另外一个函数
# 函数调用遵循栈结构,先进后出

# def function_a():
#     print("function_a:first")
#     function_b()
#     print("function_a:last")
# def function_b():
#     print("function_b:first")
#     function_c()
#     print("function_b:last")
#
# def function_c():
#     print("function_c")
#
# function_a()
#运行结果:
# function_a:first
# function_b:first
# function_c
# function_b:last
# function_a:last

# #案例1:定义一个函数:根据传入的底和高计算三角形面积的函数
# def triangle_area(base, height):
#     return base * height / 2
# print(triangle_area(5, 4))
# #案例2:定义一个函数:计算传入的字符串中元音字母的个数(aeiouAEIOU)
# def vowel_letters(word):
#     num = 0
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for letter in word:
#         if letter in vowels:
#             num += 1
#     return num
# print(vowel_letters('hello'))
# #案例3:定义一个函数:计算传入的班级学员高考成绩列表中成绩的最高分  最低分  平均分(保留一位小数),并返回
# def score(score_list):
#     max_score = max(score_list)
#     min_score = min(score_list)
#     avg_score  = sum(score_list) / len(score_list)
#     return max_score, min_score, round(avg_score,1)
#
# max_score, min_score, avg_score = score([455, 527, 639, 564, 555,657])
# print(max_score, min_score, avg_score)

#需求1：定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# - 分数 >= 90：A
# - 分数 >= 75：B
# - 分数 >= 60：C
# - 分数 < 60：D

def score_scale(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

print(score_scale(100))
print(score_scale(70))

#需求2：定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
#把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("level"))
print(is_palindrome("radar"))
print(is_palindrome("python"))

#需求3：定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def time_conversion(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds
print(time_conversion(10))
print(time_conversion(4211))

#需求4：定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
def triangle_type(a,b,c):
    if a + b <= c or b + c <= a or a + c <= b:
        return "不能构成三角形"
    elif a == b == c:
        return "等边三角形"
    elif a == b or b == c or a == c:
        return "等腰三角形"
    else:
        return "普通三角形"

print(triangle_type(2, 2, 2))
print(triangle_type(2,3,3))
print(triangle_type(2,3,6))
print(triangle_type(2,3,4))
