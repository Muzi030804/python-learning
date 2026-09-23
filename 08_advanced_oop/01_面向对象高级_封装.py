"""
1.私有属性: 在属性名前加双下划线__
2. 私有方法: 在方法名前加双下划线__


"""

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

if __name__ == '__main__':
    car = Car("Audi","A6","black",'木梓')
    print(car.brand)
    print(car.model)
    print(car.color)

    # print(car.__owner)    报错:AttributeError: 'Car' object has no attribute '__owner'
    print(car._Car__owner)  #因为没有真正的私有机制,还是可以调用私有属性

    car.start()
    car.run()
    car.stop()
    # car.__control_fuel()    报错
    car._Car__control_fuel()    #因为没有真正的私有机制,还是可以调用私有方法
    print(car.get_owner())