#列表一次可以存储多个数据
#定义:  列表名称 = [元素1,元素2,元素3...]
#列表可以存储不同类型的元素  可以同时存int float bool str等
#元素有序,可以重复,元素可以修改
#索引:        s[0],s[1],s[2],s[3]
#支持反向索引: s[-4],s[-3],s[-2],s[-1]   从-1
#
# s = [12,33,22,34,"a"]
# print(s[0])
# print(s[-5])  #都是12
#
# #修改
# s[4] = "b"
# print(s)
#
# #删除
# del s[4]
# print(s)
#
# #遍历
# for item in s:
#     print(item)

#切片:对操作的数据截取其中一部分       列表,字符串,元组都支持切片
#语法:  序列数据[开始索引:结束索引:步长]
#包含开始索引对应的元素,不包含结束索引对应的元素,开始索引默认为0,结束索引未指定默认为列表长度,步长默认为1
#索引正向,反向都可以
# s = ["a","b","c","d","e","f"]
#
# l = s[:5]   #['a', 'b', 'c', 'd', 'e']
# print(l)
# l = s[5:]   #['f']
# print(l)
# l = s[:]    #['a', 'b', 'c', 'd', 'e', 'f']
# print(l)
# l = s[0:4:2]    #['a', 'c']
# print(l)
# l = s[5:1:-1]   #['f', 'e', 'd', 'c']
# print(l)
# l = s[1:1]  #[]    开始索引和结束索引指向同一个时为空
# print(l)
# l = s[-6:-1]    #['a', 'b', 'c', 'd', 'e']
# print(l)
# l = s[-1:-6]  #[]
# print(l)
# l = s[0:-5]  #['a']
# print(l)

#练习1：将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# list4 = list1 + list2 + list3
# merge_list = [*list1, *list2, *list3]
# print("合并后的原始列表为: ", merge_list)
# new_list = []
#
# for item in merge_list:
#     if item not in new_list:
#         new_list.append(item)
#
# print("去重后的列表为: ", new_list)


#练习2：将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# new_list = []
# for num in list4:
#     if num % 3 == 0 or num % 5 == 0:
#         new_list.append(num**2)
# print(new_list)
#练习3： 将如下列表中的正数提取出来，封装为一个新的列表。
# list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
# new_list = []
# for i in list5:
#     if i > 0:
#         new_list.append(i)
# print(new_list)

#列表的常用方法
# append()   在列表尾部加元素  s.appen(10000)
# insert()   在指定索引前,插入该元素  s.insert(0,92)
# remove()   移除列表中第一个匹配到的值  s.remove(75)
# pop()      删除列表中指定索引位置的元素(如果未指引,默认最后一个)  s.pop(2)/s.pop()
# sort()     对列表元素进行排序(列表元素的数据类型一致,才可以进行排序)  s.sort()
# reverse()  反转列表元素  s.reserve()
# sum()      求和         sum(s)
# len()      数组中多少元素    len(s)
#
s = [11, 2, 31, 4, -5, 15, 17, 28]
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28]
s.append(10)
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28, 10]
s.insert(1,10)
print(s)    #[11, 10, 2, 31, 4, -5, 15, 17, 28, 10]
s.remove(10)
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28, 10]
s.pop()
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28]
s.sort()
print(s)    #[-5, 2, 4, 11, 15, 17, 28, 31]
s.reverse()
print(s)    #[31, 28, 17, 15, 11, 4, 2, -5]
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list1.sort()
print(list1)

#案例:将输入的10个数字,存储到一个列表中,并排序,输出其中的最小值,最大值和平均值
# list1 = []
# for i in range(10):
#     num = int(input("输入一个数字:"))
#     list1.append(num)
# print(list1)
# list1.sort()
# print(list1)
# print(f"最小值为:{list1[0]}")
# print(f"最大值为:{list1[9]}")
# print(f"最大值为:{list1[-1]}")
#
# s = 0
# for i in list1:
#     s += i
# print(f"平均值为:{s/10}")
# print(f"平均值为:{sum(list1)/len(list1)}")


#合并两个列表中的元素,并对合并后的结果进行去重
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# # new_list = [*num_list1, *num_list2]    三种合并方式
# # new_list = num_list1 + num_list2
# new_list = num_list1
# for i in num_list2:
#     num_list1.append(i)
#
# print("合并后的列表为:", new_list)
# l = []
# for num in new_list:
#     if num not in l:
#         l.append(num)
# print(f"去重后的数组为:{l}")

#生成1~20的平方列表
# l = []
# for i in range(1,21):
#     l.append(i**2)
# print(l)
#方法二:列表推导式    按照一定的规则快速生成一个列表  语法格式1:   [要插入的值 for  i  in 序列/列表]
# num_list = [i**2 for i in range(1,21)]
# print(num_list)


#从如下数字列表中提取所有偶数,并计算其平方,组成新的列表
num_list = [19,23,54,64,97,20,109,232,123,43,26,55,72]
l = []
for num in num_list:
    if num % 2 == 0:
        l.append(num**2)
print(l)
#方法二:列表推导式   语法格式2:     [要插入的值 for  i  in 序列/列表 if 条件]
new_list = [ i**2 for i in num_list if i % 2 == 0]
print(new_list)