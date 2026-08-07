#集合
#无序,不可重复,可修改
#定义
# s1 = {"c","d","e","f","g","c","e"}
# print(s1)       #{'e', 'f', 'd', 'c', 'g'}  无序,但去重
# print(type(s1)) #<class 'set'>
# #空集合
# s2 = set()      #不可以使用{},{}表示的是空字典,由于集合是无序的,因此不支持小标索引
# print(s2)       #set()  表示空集合
# print(type(s2)) #<class 'set'>
from os import remove

#常用方法
#add()          添加元素到集合                                 s.add('t')
#remove()       移除集合中指定元素(不存在则报错)                  s.remove('t')
#pop()          随机删除集合中的元素并返回                       e = s.pop()
#clear()        清空集合                                        s.clear()
#difference()   求两个集合的差集(第一个集合有,第二个集合没有的元素)   s1.difference(s2)
#union()        求两个集合的并集                                s1.union(s2)
#intersection   求两个集合的交集                                s1.intersection(s2)
# s1 = {100,200,300,400,500,600,700,800}
# s1.add(1200)
# print(s1)       #{800, 100, 200, 300, 400, 1200, 500, 600, 700}
#
# s1.remove(200)
# print(s1)       #{800, 100, 300, 400, 1200, 500, 600, 700}
#
# e = s1.pop()
# print(e)        #800
# print(s1)       #{100, 300, 400, 1200, 500, 600, 700}
#
# s1.clear()
# print(s1)       #set()
#
# s2 = {"A","B","C","D","E","X","Y"}
# s3 = {"C","E","Y","Z"}
# print(s2.difference(s3))        #{'B', 'D', 'A', 'X'}
# print(s2.union(s3))             #{'Y', 'D', 'Z', 'A', 'X', 'B', 'E', 'C'}
# print(s2.intersection(s3))      #{'E', 'Y', 'C'}

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
#1.找出同时选择了法语和艺术的学生  &也可以表示交集&
print(f"同时选择了法语和艺术的学生:{french_set.intersection(art_set)}")
print(f"同时选择了法语和艺术的学生:{french_set & art_set}")

#2.找出同时选择所有四门课程的学生
print(f"同时选择所有四门课程的学生:{football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)}")
print(f"同时选择所有四门课程的学生:{football_set & basketball_set & french_set & art_set}")

#3.找出选择了足球,但是没有选择篮球的学生  -(减号)也可以表示差集
print(f"找出选择了足球,但是没有选择篮球的学生:{football_set.difference(basketball_set)}")
print(f"找出选择了足球,但是没有选择篮球的学生:{football_set - basketball_set}")
#还可以通过集合推导式     快速构建集合,语法:    {要往集合中添加的元素   for s in set if 条件}
s1 = {s for s in football_set if s not in basketball_set}
print(f"找出选择了足球,但是没有选择篮球的学生:{s1}")

#4.统计每一个学生的课程数量
# name = football_set.union(basketball_set).union(art_set).union(french_set)
#也可以用  |表示并集
name = football_set | basketball_set | french_set | art_set
#因为集合中元素不能重复,因此可以用列表
all_list = [*football_set, *basketball_set, *french_set, *art_set]
for n in name:
    print(f"{n}选择的课程数量为:{all_list.count(n)}")
#笨方法
# for n in name:
#     num = 0
#     if n in football_set:
#         num += 1
#     if n in basketball_set:
#         num += 1
#     if n in art_set:
#         num += 1
#     if n in french_set:
#         num += 1
#     print(f"{n}选择的课程数量为:{num}")
