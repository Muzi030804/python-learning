# 魔法方法是指Python中提供的以双下划线开头和结尾的特殊方法,用于定义类的特殊行为,比如:__init__
# 魔法方法不需要手动调用,Python会在合适的时机自动调用

class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f"{self.brand} {self.name} 正在行驶...")
    def __str__(self):      #将print(对象)转化为字符串
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self, other):        #两个对象之间使用 == 会自动调用__eq__
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):                ##两个对象之间使用 < 会自动调用__lt__,如果使用 > ,相当于取反,也可以调用
        return self.price < other.price

c1 = Car("BWM","X5",500000)
print(c1)       #<__main__.Car object at 0x7f3e39e9b230>    加入__str__后:    BWM X5 500000

c2 = Car("BWM","X5",500001)
print(c2)       #<__main__.Car object at 0x7f3e39e79f90>    加入__str__后:    BWM X5 500000

print(c1 == c2)     #False  如果直接比较两个对象,会基于对象的内存地址进行比较    加入__eq__后:   False(因为价格不一样)
print(c1 < c2)      #报错:TypeError: '<' not supported between instances of 'Car' and 'Car'   加入__lt__后:      True

