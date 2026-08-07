#元组一旦创建不能修改
#可以存储不同类型的元素
#元素可以重复,有序,不可以修改,支持索引访问,切片
#定义元组
#元组名称 = (元素1,元素2...)
#t1 = (1,5,6,9,6,4)
#定义空元组
#元组名称 = ()
#t2 = ()
#元组名称 = tuple()
#t3 = tuple()
#因为不能修改,所以只支持查询,统计操作
#count()  统计某元素出现的次数
#index()  查找某个元素在元组中的索引位置(第一次出现的位置)
# t1 = (1,5,6,9,6,4)
# print(type(t1))     #<class 'tuple'>
# print(t1[0])        #1
# print(t1[-1])       #4
#
# print(t1.count(6))  #2
# print(t1.index(5))  #1
from unittest import skipUnless

#切片
# print(t1[1:4])  #(5, 6, 9)

#定义单个元素的元组   要在后面加逗号
# t2 = (100)   #int
# print(type(t2)) #<class 'int'>
# t3 = (100,)     #tuple
# print(type(t3))  #<class 'tuple'>

#组包(Packing):将多个值合并到一个容器(元组或列表)中
#解包(Unpacking):将容器(元组或列表)解开成独立的元素,分别赋值给多个变量
#定义元组,组包
# t1 = (5,7,9,1)  #组包
# t2 = 5,7,9,1    #组包
# #基础解包
# a,b,c,d = t1
# print(a,b,c,d)  #5 7 9 1
# # q,w,r = t1    #报错:too many values to unpack
# # print(q,w,r)
# # a,b,c,d,e = t1  #报错:not enough values to unpack
# # print(a,b,c,d,e)
# #(*)扩展解包   元组解包时, * 表示收集剩下的所有元素,生成列表
# x,*y,z = t2    #x为5,y为[7,9],z为1
# s, *o = t2      #s为5,o为[7,9,1]
# *o, e = t2     #o为[5,7,9],e为1

# #案例1:现有两个变量,分别为a = 10, b = 20 现需要将两个变量值交换,然后输出
# a = 10
# b = 20
# # t = a,b
# # b,a = t
# #这两行可以简化为
# a,b = b,a
# print("b:",b)
# print("a:",a)
#
# #案例2:现有三个变量,分别为a = 100, b = 200,c = 300, 现需要将三个变量值交换,将a,b,c的值分别赋给c,a,b然后输出
# a,b,c = 100,200,300
# # t = a,b,c
# # c,a,b = t
# #简化为
# c,a,b = a,b,c
# print("c",c)
# print("a",a)
# print("b",b)

#根据学生成绩单完成以下需求:
# 1.计算各个学生的总分,各科平均分,然后一并输出
# 2.统计各科成绩的最低分  最高分  平均分,并输出
# 3.查找成绩优秀(平均分>90)的学生,并输出
students =(
    ("S001","a",85,92,78),
    ("S002","b",92,88,95),
    ("S003","c",78,85,82),
    ("S004","d",88,79,91),
    ("S005","e",95,96,89),
    ("S006","f",76,82,77),
    ("S007","g",89,91,94),
    ("S008","h",75,69,82),
    ("S009","i",86,89,98),
    ("S010","j",66,59,72),
)
print(students)
# 1.计算各个学生的总分,各科平均分,然后一并输出
#方法一
# for stu in students:
#     print(f"学生{stu[1]}的总分为:{stu[2]+stu[3]+stu[4]}")
#     print(f"学生{stu[1]}的平均分为:{(stu[2]+stu[3]+stu[4])/3:.1f}")
#方法二
for uid,name,chinese_score,math_score,english_score in students:
    total = chinese_score + math_score + english_score
    avg = total /3
    print(f"学生{name}的总分为:{total}")
    print(f"学生{name}的平均分为:{avg}")
# 2.统计各科成绩的最低分  最高分  平均分,并输出

#获取成绩列表  简介写法  可以使用max(),min(),sum()
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文最低分为:{min(chinese_scores)},最高分为:{max(chinese_scores)},平均分为:{sum(chinese_scores)/len(chinese_scores):.1f}")
print(f"数学最低分为:{min(math_scores)},最高分为:{max(math_scores)},平均分为:{sum(math_scores)/len(math_scores):.1f}")
print(f"英语最低分为:{min(english_scores)},最高分为:{max(english_scores)},平均分为:{sum(english_scores)/len(english_scores):.1f}")
# chinese_min = students[0][2]
# chinese_max = students[0][2]
# math_min = students[0][3]
# math_max = students[0][3]
# english_min = students[0][4]
# english_max = students[0][4]
# chinese_sum =0
# math_sum = 0
# english_sum = 0
# for stu in students:
#     if stu[2] < chinese_min:
#         chinese_min = stu[2]
#     if stu[3] < math_min:
#         math_min = stu[3]
#     if stu[4] < english_min:
#         english_min = stu[4]
#     if stu[2] > chinese_max:
#         chinese_max = stu[2]
#     if stu[3] > math_max:
#         math_max = stu[3]
#     if stu[4] > english_max:
#         english_max = stu[4]
#     chinese_sum+=stu[2]
#     math_sum+=stu[3]
#     english_sum+=stu[4]
# chinese_avg = chinese_sum / len(students)
# math_avg = math_sum / len(students)
# english_avg = english_sum / len(students)
# print(f"语文最低分为:{chinese_min},最高分为:{chinese_max},平均分为:{chinese_avg:.1f}")
# print(f"数学最低分为:{math_min},最高分为:{math_max},平均分为:{math_avg:.1f}")
# print(f"英语最低分为:{english_min},最高分为:{english_max},平均分为:{english_avg:.1f}")
# 3.查找成绩优秀(平均分>90)的学生,并输出
#写法一:
# for stu in students:
#     if (stu[2]+stu[3]+stu[4])/3 > 90:
#         print(f"{stu[1]}的成绩优秀,学号为:{stu[0]},平均分为:{(stu[2]+stu[3]+stu[4])/3:.1f}")
#写法二:
for uid,name,chinese_score,math_score,english_score in students:
    total = chinese_score + math_score + english_score
    avg = total /3
    if avg > 90:
        print(f"学号:{uid},姓名:{name},平均分:{avg:.1f}")
