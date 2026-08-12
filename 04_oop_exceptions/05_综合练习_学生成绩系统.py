# 采用面向对象的编程思想,开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2. 修改学生信息：根据输入的学生姓名,修改对应的学生成绩
# 3. 删除学生信息：根据输入的学生姓名,删除对应的学生成绩
# 4. 查询学生信息：根据输入的学生姓名,查找对应的学生成绩,并输出
# 5. 列出所有学生：展示所有学生信息并输出。
# 6. 退出系统。


class Student:


    def __init__(self,name,chinese_score,math_score,english_score):
        self.name = name
        self.chinese_score = chinese_score
        self.math_score = math_score
        self.english_score = english_score

    def __str__(self):
        return f"姓名:{self.name} 语文:{self.chinese_score} 数学:{self.math_score} 英语:{self.english_score} 总分:{self.chinese_score + self.math_score + self.english_score}"

    def update_score(self,chinese_score=None,math_score=None,english_score=None):
        if chinese_score is not None:
            self.chinese_score = chinese_score
        if math_score is not None:
            self.math_score = math_score
        if english_score is not None:
            self.english_score = english_score

class EduManagement:
    def __init__(self):
        self.student_list = []

    #添加学生信息
    def add_student(self):
        name = input("输入学生姓名:")
        for stu in self.student_list:
            if stu.name == name:
                print("该学生已存在")
                return
        chinese_score = int(input("请输入语文成绩:"))
        math_score = int(input("请输入数学成绩:"))
        english_score = int(input("请输入英语成绩:"))

        if 0<= chinese_score <= 100 and 0<= math_score <= 100 and 0<= english_score <= 100:
            stu = Student(name,chinese_score,math_score,english_score)
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("成绩要在0~100之间")

    #修改学生信息
    def update_score(self):
        name = input("输入要修改的学生姓名:")
        for stu in self.student_list:
            if stu.name == name:
                print(f"当前成绩:{stu}")
                chinese_score = int(input("请输入语文成绩:"))
                math_score = int(input("请输入数学成绩:"))
                english_score = int(input("请输入英语成绩:"))
                if 0 <= chinese_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
                    stu.update_score(chinese_score,math_score,english_score)
                    print("学生信息修改成功")
                    print(f"修改后的成绩为:{stu}")
                    return
                else:
                    print("成绩要在0~100之间")
                    return
        print("未找到该学生")

    #删除学生信息
    def del_student(self):
        name = input("输入要删除的学生姓名:")
        for stu in self.student_list:
            if stu.name == name:
                self.student_list.remove(stu)
                print("删除成功")
                return
        print("该学生不存在")

    #查询学生信息
    def query_student(self):
        name = input("输入要删除的学生姓名:")
        for stu in self.student_list:
            if stu.name == name:
                print(f"学生信息为:{stu}")
                return
        print("未找到该学生")

    #查询全部信息
    def query_all(self):
        for stu in self.student_list:
            print(stu)

    #运行系统
    def run(self):
        print("欢迎使用")

        while True:
            print()
            print("################################################")
            print("1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统")
            print("#################################################")

            choice = input("选择操作:")

            try:
                match choice:
                    case '1':
                        self.add_student()
                    case '2':
                        self.update_score()
                    case '3':
                        self.del_student()
                    case '4':
                        self.query_student()
                    case '5':
                        self.query_all()
                    case '6':
                        print("退出系统")
                        return
                    case _:
                        print("输入错误,请选择1~6")
            except ValueError as e:
                print("输入的数字有问题,请重新选择",e)
            except Exception as e:
                print("程序出错,请重新选择",e)


if __name__ == '__main__':
    manage = EduManagement()
    manage.run()

