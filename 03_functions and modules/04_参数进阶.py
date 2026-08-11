# 参数进阶学习记录

# 传参方式:在调用函数时,传递实参的方式
# 1.位置参数:调用时根据函数定义时的位置来传递参数    要求调用函数时参数顺序与定义函数时参数顺序完全一致
#
# 2.关键字参数:调用函数时以函数定义时形参名称作为关键字,以"键=值"的形式来传递(不要求顺序)
# def reg_stu(name,age,gender,city):
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
# #位置参数
# stu = reg_stu("小王",23,"男","重庆")
# print(stu)
# #关键字参数
# stu = reg_stu(name="张三",age=18,gender="男",city="北京")
# print(stu)
# #与顺序无关
# stu2 = reg_stu(gender="男",name="李四",city="上海",age=22)
# print(stu2)
# #如果位置参数与关键字参数混用,关键字参数必须在位置参数之后(关键字参数之间,没有顺序要求)
# stu3 = reg_stu("王五",25,city="上海",gender="男")
# print(stu3)

#默认参数
#默认参数也称为缺省参数,用于在定义函数时,为参数提供默认值,调用函数时,可以不传递有默认值的参数
# def reg_stu(name,age,gender="男",city='北京'): #默认参数必须放在没有默认值的参数列表的后面,一个函数在定义时可以设置多个默认参数
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
# #函数调用时,如果默认参数传递了值,则会修改默认的参数值,如果没有传递该参数,则直接使用默认值
# stu = reg_stu("张三",18)
# print(stu)
# stu = reg_stu("李四",22,"男","南京")
# print(stu)
# stu = reg_stu("王五",24,city="南京")
# print(stu)

#不定长参数  函数参数个数不固定
# 不定长参数也叫可变参数,用于函数定义及调用时参数个数不确定(0个或多个)的场景()
# 类型     位置传递     关键字传递
#
# 不定长参数-位置传递(*args)  传递的所有匹配的未知参数都会被args变量收集,这些参数会合并封装为一个元组,args是元组类型(注意并不会封装关键字参数)
# *args只是约定俗成的变量名,并不是关键字,可以使用任何合法的变量名(如*data)
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data,1)
# data = calc_data(10, 20, 30, 40)
# print(data)
# data = calc_data(100, 200, 300, 400)
# print(data)

# 不定长参数-关键字传递(**kwargs)      参数是以"键=值"形式传递的关键字参数,这些"键=值"参数都会被kwargs接受,并合并为一个字典类型
# **kwargs只是约定俗成的变量名,并不是关键字,可以使用任何合法的变量名(如**options)
def calc_data(*args,**kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get('round') is not None:
        avg_data = round(avg_data,kwargs.get('round'))

    if kwargs.get('print'):
        print(min_data,max_data,avg_data)

    return min_data,max_data,avg_data

data = calc_data(100,200,301,round=2,print=True)  #100 301 200.33 round作用是几位小数 print表示是否打印
print(data)     #(100, 301, 200.33)

data = calc_data(33,32,13,45,35,67)     #无print,因为不满足kwargs.get('print') == True
print(data)     #(13, 67, 37.5)