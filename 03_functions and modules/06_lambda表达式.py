# lambda 表达式学习记录

# 匿名函数指的是没有名称的函数,需要通过lambda表达式来声明函数,可以简化简单函数的编写(单行表达式)
# 注意:函数逻辑比较简单(单行表达式)且只在一个地方使用时,可以考虑使用匿名函数,简化书写(通常作为高阶函数的参数使用)
# 注意:匿名函数中可以返回结果,也可以不返回结果,返回结果是不需要写return,表达式的运行结果就是要返回的结果
#定义匿名列表
#lambda 参数列表 : 函数体              没有函数名

#需求1:打印一个分隔线
# def out_line():
#     print('------------')
# out_line = lambda : print('-------------')  #匿名函数无法直接调用,所以需要赋值给变量,这个变量是一个函数
# out_line()
# #需求2:计算两数之和
# # def add(x,y):
# #     return x+y
# add = lambda x,y: x+y          #lambda表达式会自动将结果返回,不需要写return
# print(add(3,4))

#需求3:完成如下列表的排序操作,按照每一个元素的字符个数从小到大排序    匿名函数典型应用场景
data_list = ["C++","C","Python","Java","PHP","Go","JavaScript"]
data_list.sort(key=lambda item : len(item))         #sort函数中的参数key,表示按什么排序,key是一个函数
print(data_list)

