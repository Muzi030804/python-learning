# 函数作为参数学习记录

# 普通参数:int,bool,str,list,tuple,set,dict等
# 特殊参数:函数

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def calculate(x,y,oper):        #oper是函数
    return  oper(x,y)           #函数调用语法

result = calculate(2,3,add)
print(result)
result = calculate(2,3,subtract)
print(result)
