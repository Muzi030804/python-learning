#继承(重写)
# 如果重写时要调用父类方法
# 方式一: super().方法名()
# 方式二: 类名.方法名(self)
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

# 智驾
class AiDrive:
    """
    AI 智能驾驶
    """
    def __init__(self,version="v1.0"):
        self.version = version

    def run(self):
        print(f"使用AI智能驾驶系统{self.version}正在行驶")

# 问界
class WenjieCar(Car,AiDrive):
    def __init__(self,brand,model,color,owner,version):
        Car.__init__(self,brand,model,color,owner)
        AiDrive.__init__(self,version)

    def run(self):
        Car.run(self)
        AiDrive.run(self)

# MRO: Method Resolution Order 方法解析顺序
if __name__ == '__main__':
    print(WenjieCar.__mro__)  # 方法解析顺序: (<class '__main__.WenjieCar'>, <class '__main__.Car'>, <class '__main__.AiDrive'>, <class 'object'>)
    print(WenjieCar.mro())  # 方法解析顺序: [<class '__main__.WenjieCar'>, <class '__main__.Car'>, <class '__main__.AiDrive'>, <class 'object'>]
    c = WenjieCar("Audi","A6","black",'木梓','1.1')
    print(c.__dict__)

    c.run()
    #Audi A6 正在行驶...
    #使用AI智能驾驶系统1.1正在行驶