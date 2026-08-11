# 类型注解学习记录

#类型注解是python中的一种语法特性,用于明确表示变量,函数参数和返回值的数据类型,从而使代码更清晰,更安全,更易维护
a = 100
b:int = 100
names : list[str] = ["A", "B", "C"]         #
phone: set[str | int] = {"15915246633", "15915246634", "15915246635",12222555}
options:dict[str, int] = {"count":0,"total":0}
goods: tuple[str,int,int] = ("phone",2333,3)

#函数类型注解
#为函数添加类型注解,其实主要就是为函数的参数和返回值添加类型注解

def circle_area_len(r: float) ->tuple[float,float]:
    return round(3.14 *r *r,1),round(2 * 3.14 * r,1)