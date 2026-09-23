"""
某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
核心功能：
会员登录：会员通过卡号和密码登录系统
借书：会员可以借阅库存中有余量的图书
还书：会员可以归还借阅的图书
查看我的借阅：展示当前会员已经借阅的图书列表
退出系统
借阅规则：
普通会员最多可借3本
VIP会员最多可借6+VIP等级（VIP等级，默认为1）
注意：
登录成功（卡号和密码均正确）后，才可以访问该系统
图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书
"""
from abc import ABC, abstractmethod
import json

class Book:
    def __init__(self,book_id,title,author,total_num):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def borrow_book(self):  #借阅书籍
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):  # 归还书籍
        self.__available_num += 1
        return True

    def get_available_num(self):    #获取可用数量
        return self.__available_num

# 抽象类: 是一种只能被继承, 不能被直接实例化的类(不能直接创建对象), 作用就是规定子类必须要实现哪些方法, 强制子类必须遵守统一的代码规范
# Python中的抽象类, 需要继承 abc 模块中的 ABC 类 ,ABC: Abstract Base Class
# 会员类
class Member(ABC):
    def __init__(self, card_id, name, password):
        self.name = name
        self.card_id = card_id
        self.__password = password
        self.__borrowed_books = []

    def borrow_book(self, book: Book):
        # 借阅数量是否达到限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅数量达到限制")
            return False

        # 判断书籍是否可借
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name} borrowed book {book.title}")
            return True
        else:
            print(f"借阅失败: 图书{book.title}已被借完")
            return False

    def return_book(self,book: Book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} returned book {book.title}")
        else:
            print(f"归还失败,没有借阅该书籍{book.title}")

    def get_password(self):
        return self.__password
    def get_borrowed_books(self):
        return self.__borrowed_books

    # 获取会员最大借阅数量
    @abstractmethod
    def get_max_books(self) -> int:
        pass

class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3

class VIPMember(Member):
    def __init__(self,card_id,name,password,vip_level):
        self.vip_level = vip_level
        super().__init__(card_id,name,password)

    def get_max_books(self) -> int:
        return self.vip_level + 6

# 图书馆管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.current_member: Member | None = None
        # 加载数据
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book["编号"]] = Book(book["编号"],book["标题"],book["作者"],book["数量"])
            print("加载书籍数据成功")



    def load_members_data(self):
        with open("data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'].startswith("N"):
                    self.members[member['卡号']] = NormalMember(member['卡号'],member['姓名'],member['密码'])
                elif member['卡号'].startswith("V"):
                    self.members[member['卡号']] = VIPMember(member['卡号'],member['姓名'],member['密码'],member['会员等级'])
            print("会员数据加载完成")

    # 登录
    def login(self):
        while True:
            print("[登录]")
            member_id = input("请输入会员卡号:")
            password = input("请输入会员密码:")

            # 判断卡号是否存在
            if member_id not in self.members:
                print("登录失败,卡号不存在")
                continue

            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                print("登陆成功")
                self.current_member = member
                return True
            else:
                print("登录失败,密码错误")
                continue

    def borrow_book(self):
        # 展示图书列表
        for book in self.books.values():
            print(f"编号:{book.book_id},标题:{book.title},作者:{book.author},总数:{book.total_num},可用:{book.get_available_num()}")

        #获取用户输入的图书编号,执行结束操作
        book_id = input("请输入要借阅的图书编号")
        if book_id not in self.books:
            print("图书不存在")
            return
        self.current_member.borrow_book(self.books[book_id])
        #
    def return_book(self):
        # 展示出当前会员的借阅列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("借阅的书籍如下:")
        for book in borrowed_books:
            print(f"编号:{book.book_id},标题:{book.title}")
        # 获取用户输入的图书编号,执行还书操作
        book_id = input("请输入要归还的图书编号")
        if book_id not in self.books:
            print("还书失败,编号不存在")
            return
        self.current_member.return_book(self.books[book_id])

    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("已借阅的书籍如下:")
            for book in borrowed_books:
                print(f"编号:{book.book_id},标题:{book.title}")
        else:
            print("当前没有借阅任何图书")



    def run(self):
        if self.login():
            while True:
                print("\n1. 借阅")
                print("2. 归还")
                print("3. 查看")
                print("4. 退出")

                choice = input("请选择操作1-4")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统")
                        break
                    case _:
                        print("无效的选项,请重新选择")

if __name__ == '__main__':
    lib = LibrarySystem()
    lib.run()