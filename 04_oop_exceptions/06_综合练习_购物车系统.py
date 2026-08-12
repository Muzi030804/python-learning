"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""

class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称:{self.name}  价格:{self.price}  商品数量:{self.num}"

    def update_price(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num  is not None:
            self.num = num
class ShoppingCart:
    def __init__(self):
        self.shopping_cart_list = []

    #添加购物车
    def add_shopping_cart(self):
        name = input("输入添加的商品名称:")
        for good in self.shopping_cart_list:
            if good.name == name:
                print("该学生已存在")
                return
        price = float(input("输入价格:"))
        num = int(input("输入数量:"))
        self.shopping_cart_list.append(Goods(name,price,num))
        print("添加完成")

    #修改购物车
    def update_shopping_cart(self):
        name = input("输入修改的商品名称:")
        for good in self.shopping_cart_list:
            if good.name == name:
                price = float(input("输入价格:"))
                num = int(input("输入数量:"))
                good.update_price(price,num)
                print("修改完成")
                return
        print("该商品不存在")

    #删除购物车
    def delete_shopping_cart(self):
        name = input("输入删除的商品名称:")
        for good in self.shopping_cart_list:
            if good.name == name:
                self.shopping_cart_list.remove(good)
                print("删除完成")
                return
        print("该商品不存在")

    #查询购物车
    def show_shopping_cart(self):
        for good in self.shopping_cart_list:
            print(good)

    def run(self):

        while True:
            print()
            print("#########################################")
            print("1.添加信息  2.修改信息  3.删除信息  4.查询信息  5.退出系统 ")
            print("#########################################")
            choice = input("选择操作:")
            try:
                match choice:
                    case '1':
                        self.add_shopping_cart()
                    case '2':
                        self.update_shopping_cart()
                    case '3':
                        self.delete_shopping_cart()
                    case '4':
                        self.show_shopping_cart()
                    case '5':
                        print("退出成功")
                        return
                    case _:
                        print("请输入1~5")
            except Exception as e:
                print("程序错误,请重新输入")

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.run()
