# 变量作用域学习记录

#变量的作用域指的是变量的作用范围
# 全局变量:函数之外,整个文件中都可以使用,通常定义在文件顶部
# 局部变量:函数内部,只能在函数内部使用

num = 100
def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    num = 1000              #这是局部变量num,和全局变量num不是同一个num
    print("num:",num)
    return area
print(circle_area(10))
print("num:",num)           #num: 100   这是全局变量num

#global关键字:在函数中要使用全局变量,使得可以在函数内部修改全局变量的值

num = 1
def fun1():
    global num          #声明  使用全局变量num
    num = 100
    print("num:",num)

fun1()                  #num: 100
print("num:",num)       #num: 100
