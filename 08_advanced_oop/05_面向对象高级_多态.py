#多态

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand      #公有属性
        self.model = model      #公有属性
        self.color = color      #公有属性
        self.__owner = owner    #私有属性

    def start(self):
        print(f"{self.brand} {self.model} 正在启动...")

    def run(self):
        print(f"{self.brand} {self.model} 正在行驶...")

    def stop(self):
        print(f"{self.brand} {self.model} 停止行驶...")

    def __control_fuel(self):
        print(f"{self.brand} {self.model} 正在控制油门...")

    def get_owner(self):    #用公共方法可以调用私有属性
        return self.__owner[:1] + "**"

    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料...")

# 燃油车
class FuelCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} 正在加油...")

# 电车
class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} 正在充电...")

# 补充燃料函数
def handle_charge(car: Car):
    car.charge()

if __name__ == '__main__':
    handle_charge(FuelCar("Audi","A6","black",'木梓'))        #Audi A6 正在加油...
    handle_charge(ElectricCar("BYD","汉","black",'木梓'))     #BYD 汉 正在充电...