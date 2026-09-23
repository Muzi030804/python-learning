
#继承
# class Car(Object)  默认继承Object类
# 私有的属性和方法不能够继承
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

# 燃油车
class FuelCar(Car):
    pass

# 电车
class ElectricCar(Car):
    pass

if __name__ == '__main__':
    c1 = FuelCar("Audi","A6","black",'木梓')
    c1.start()
    c1.run()
    c1.stop()
    print(c1.brand, c1.model, c1.get_owner(),c1.color)

