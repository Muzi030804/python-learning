# 属性:
# 实例属性:实例属性属于每个具体对象的属性,每个对象都是独立的(各个对象特有的数据)
# 类属性:雷属性是属于类本身的属性,所有实例共享的(所有对象共享的数据或配置)
# 说明:通过实例查找属性时,会先查找实例属性,实例属性不存在时,在查找类属性

class Car:
    #类属性(所有实例对象共享)  通过 类名.属性 的方式操作
    wheel = 4       #轮胎数量
    tax_rate = 0.1  #购置税

    def __init__(self,brand,name,price):
        # 实例属性,通过 实例对象.属性 的方式操作
        self.brand = brand
        self.name = name
        self.price = price
        self.wheel = 2

    def running(self):
        print(f"{self.brand} {self.name}正在行驶...")

    def total_price(self, discount, rate=0.1):
        """
        计算提车总费用
        :param discount: 折扣
        :param rate: 税率
        :return: 总费用
        """
        total_price = self.price * discount + self.price * rate
        return total_price

c1 = Car("BWM", "X5", 500000)
print(Car.wheel)        #4
print(c1.wheel)         #2   通过实例查找属性时,会先查找实例属性,实例属性不存在时,在查找类属性