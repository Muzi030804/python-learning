# 定义类
# class 类名:
#     def __init__(self,参数列表):
#         self.属性名 = 参数值
#         self.属性名 = 参数值
#     def 方法名(self,形参列表):
#         ...
#     def 方法名(self,形参列表):
#         ...
# 创建对象
# 对象名 = 类名(参数列表)
# 对象名.方法名(实参)

class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price


    def running(self):
        print(f"{self.brand} {self.name}正在行驶...")

    def total_price(self,discount,rate=0.1):
        """
        计算提车总费用
        :param discount: 折扣
        :param rate: 税率
        :return: 总费用
        """
        total_price = self.price*discount + self.price*rate
        return total_price

c1 = Car("BWM","X5",500000)
total1 = c1.total_price(0.9,0.2)
print(f"提车总价为:{total1:.0f}")       #提车总价为:550000
c1.running()                #BWM X5正在行驶...

c2 = Car("BWM","X5",500000)
total2 = c2.total_price(0.9)
print(f"提车总价为:{total2:.0f}")        #提车总价为:500000
