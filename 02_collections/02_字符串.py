#字符串是字符的容器,一个字符串可以放任意数量的字符    如:"Python"  'Python'  """Python"""
#特点:不可变(无法修改)    有序性    可迭代性(可以通过for循环遍历)
#字符串中的每一个字符元素都有其对应的下标,支持正向  反向索引
#字符串切片    语法: 序列对象[开始索引:结束索引:步长]
# s = "hello-world"
# print(s[4])
# print(s[-1])
#
# # s[4] = "x"   报错,不支持修改
# # print(s[4])
#
# for i in s:
#     print(i)
#
# #切片
# print(s[1:5])
# print(s[-1:-5:-1])

#字符串常用方法   无法对字符串进行任何修改
#find()     查找子串,返回第一次出现的索引位置,找不到返回-1      s.find('Python')
#count()    统计子串在字符串中出现的次数      s.count('H')
#upper()    将字符串中所有字母转换为大写      s.upper()
#lower()    将字符串中所有字母转换为小写      s.lower()
#split()    将字符串按指定分隔符分割为列表     s.split('-')
#strip()    去除字符串两端的空白字符或指定字符   s.trip()/strip('s')   默认空格
#replace()  将字符串的指定子串替换为新的子串    s.replace('H','C')
#startswith()  检查字符串是否以指定子串开头,返回bool值   s.startswith('P')
#endswith()     检查字符串是否以指定子串结尾,返回bool值   s.endswith('P')

# print(s.find('hello')) #0
# print(s.count('l'))  #3
# up_str = s.upper()
# print(up_str)       #HELLO-WORLD
# low_str = s.lower()
# print(low_str)      #hello-world
# l = s.split('-')
# print(l)            #['hello', 'world']
# ss = s.strip('l')
# print(ss)           #hello-world
# ss = " hello-world "
# print(ss)           # hello-world
# print(ss.strip())   #hello-world   把空格去除了
# sss = s.replace('l','e')
# print(sss)          #heeeo-wored
# print(s.startswith('h'))    #True
# print(s.endswith('e'))      #False
#
# print(s)   #hello-world   字符串不会变

#案例:邮箱格式验证:用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.),如果正确就输出"邮箱格式正确",否则输出"邮箱格式错误"
# email = input("请输入您的邮箱:")
# 方法一:
# if email.count("@") == 1 and email.count(".") >= 1 :
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

#方法二:    in
# if email.count("@") == 1 and "." in email:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

#需求1：输入一个字符串, 判断该字符串是否是回文(两边对称)
s = input("输入一个字符串:")
#方法一:
# num = 0     #len(s)   直接获取长度
# for char in s:
#     if char != "":
#         num+=1
# print(f"字符串长度为:{num}")
# flag = True
# for i in range(num):
#     if s[i] != s[len(s)-1-i]:
#         flag = False
# if flag:
#     print("该字符串回文")
# else:
#     print("该字符串不回文")
#方法二:
if s == s[::-1]:
    print("该字符串回文")
else:
    print("该字符串不回文")
#方法三:
flag = True
light = 0
right = len(s) -1
while light<right:
    if s[light]!=s[right]:
        flag = False
        break
    light+=1
    right-=1
if flag:
    print("该字符串回文")
else:
    print("该字符串不回文")



#需求2：将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容，遍历输出出来。
# s = []
# for i in range(10):
#     string = input("输入一个字符串:")
#     s.append(string)      #s.append(string[::-1].upper())
#     s[i] = s[i][::-1].upper()
#
# for i in s:
#     print(i)

