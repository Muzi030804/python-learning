# 定义类    语法如下:
# class 类名:
#     pass
#
# 创建对象
# 对象名 = 类名()
# 对象名.属性名1 = 属性值1
# 对象名.属性名2 = 属性值2
# 说明:类名的命名规范,遵循大驼峰命名法,每个单词的首字母大写,单词之间没有分隔符,比如:UserInfo,UserAccount
# 说明:__dict__是Python中用户自定义类实例的一个特殊属性,用于以字典形式存储对象的属性

#定义类
# class Car:
#     pass
# #创建对象
# car1 = Car()
# #动态的为对象添加属性(不推荐)
# car1.brand = 'BMW'
# car1.name = "X5"
# car1.price = 500000
# print(car1)                 #<__main__.Car object at 0x7f290da9b230>  后面是内存地址,每次运行都会发生变化
# print(car1.__dict__)        #{'brand': 'BMW', 'name': 'X5', 'price': 500000}

# 定义类  语法如下:
# class 类名:
#     def __init__(self,参数列表):
#         self.属性名 = 参数值
#         self.属性名 = 参数值
# 创建对象
# 对象名 = 类名(参数列表)
#
# 说明:定义在类的外面的称之为函数,定义在类中的函数称之为方法
# __init__:初始化方法,对象创建后会自动调用,主要用于设置对象的初始状态(设置对象属性)
# self:方法的第一个参数,表示当前创建的实例对象

#定义类
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price
        print("初始化完毕")
#创建对象
c1 = Car("BMW",'X5',500000)     #初始化完毕
print(c1.__dict__)      #{'c_brand': 'BMW', 'c_name': 'X5', 'c_price': 500000}
print(c1.c_brand)       #BMW
print(c1)               #<__main__.Car object at 0x7f0cb009b230>
c2 = Car("BMW",'X5',500000)
l = [c1,c2]
for i in l:
    print(i.__dict__)