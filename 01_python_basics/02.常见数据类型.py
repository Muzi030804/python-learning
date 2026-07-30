#通过type（）查看数据的类型
from time import process_time_ns

print(type("hello"))
print(type(10))
print(type(3.14))
print(type(True))
print(type(None))

#通过isinstance(数据，类型) 判断数据是否是指定的类型，如果是：True，不是：False
num = 10
print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, bool))

#字符串的三种定义
s1 = "hello"
s2 = 'world'
s3 = """
hello
world
"""
print(s1)
print(s2)
print(s3)

#转义字符 \'  \t（缩进）  \n（换行）
s4 = 'It\' very good'
print(s4)
print("hello\nworld")
print("hello\tworld")

#字符串拼接
s1 = "hello"
s2 = "world"

print("Hi" +","+ s1 + "," + s2 + "!")

#字符串拼接案例 根据自己的实际情况，输出个人的详细信息：“大家好，我是xx，今年xx岁，学习的专业是xx”
name = "Muzi"
age = 22
major = "computer science"
#print("大家好，我是"+name + ",今年" + age + "岁,学习的专业是" + major)
print("大家好，我是"+name + ",今年" + str(age) + "岁,学习的专业是" + major)

#字符串格式化  %s:占位符  f"内容{变量/表达式}"（推荐）
#通过%占位符 的形式完成字符串与变量的快速拼接

print("大家好，我是%s，今年%s岁，学习的专业是%s"% (name, age, major))
print(f"大家好，我是{name},今年{age}岁，学习的专业是{major}")
a = 10
b = 20
print(f"a+b = {a+b}")


