# 递归学习记录

#定义一个函数,根据传入的数字,计算该数字的阶乘
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)
print(factorial(5))